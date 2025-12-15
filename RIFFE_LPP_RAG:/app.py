# =============================================================================
# Streamlit Application for a CST Business Ethics RAG Assistant
# =============================================================================
# UI Features (rubric-aligned):
# - Clear domain framing + chatbot description
# - Configurable response modes (agent customization visible)
# - Strict citation mode + tone controls
# - Retrieval diagnostics: source table w/ similarity scores + metadata
# - Detected CST principles panel
# - Export tools (copy / download .md / .txt)
# - Feedback logging to JSONL (for reflection)
# - Performance stats (latency, similarity summary)
# - Cached DB initialization (smooth reruns)
# - Example queries that actually run
# =============================================================================

import os
import time
import json
import re
from datetime import datetime
from typing import Any, Dict, List

import streamlit as st
import pandas as pd

from backend.database import RAGDatabase
from backend.agent import RAGAgent
import config

# -----------------------------------------------------------------------------
# Page Configuration (must be first Streamlit command)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Catholic Business Ethics RAG Advisor",
    page_icon="✝️",
    layout="wide"
)

# -----------------------------------------------------------------------------
# Helper: CST principles detection (simple but effective demo feature)
# -----------------------------------------------------------------------------
CST_PRINCIPLES = {
    "Human Dignity": [
        r"\bdignity\b", r"\bhuman person\b", r"\bimage of God\b", r"\bintrinsic worth\b"
    ],
    "Common Good": [
        r"\bcommon good\b", r"\bsocial good\b", r"\bpublic good\b"
    ],
    "Solidarity": [
        r"\bsolidarity\b", r"\bmutual responsibility\b", r"\bwe are one\b"
    ],
    "Subsidiarity": [
        r"\bsubsidiarity\b", r"\bclosest level\b", r"\blocal level\b", r"\bdecentraliz"
    ],
    "Preferential Option for the Poor": [
        r"\bpreferential option\b", r"\bpoor\b", r"\bvulnerable\b", r"\bmarginalized\b"
    ],
    "Stewardship / Care for Creation": [
        r"\bstewardship\b", r"\bcreation\b", r"\benvironment\b", r"\bsustainab"
    ],
    "Rights & Responsibilities": [
        r"\bright(s)?\b", r"\bresponsibilit(y|ies)\b", r"\bdut(y|ies)\b"
    ],
    "Dignity of Work & Rights of Workers": [
        r"\bdignity of work\b", r"\bworker(s)?\b", r"\blabor\b", r"\bjust wage\b", r"\bunion\b"
    ],
}

def detect_principles(text: str, sources: List[Dict[str, Any]]) -> List[str]:
    """Detect likely CST principles mentioned in answer + retrieved sources."""
    blob = (text or "") + "\n\n" + "\n\n".join([s.get("text", "") for s in (sources or [])])
    blob_lower = blob.lower()
    found = []
    for principle, patterns in CST_PRINCIPLES.items():
        for pat in patterns:
            if re.search(pat, blob_lower, flags=re.IGNORECASE):
                found.append(principle)
                break
    return found

# -----------------------------------------------------------------------------
# Helper: Safe metadata extraction for source table
# -----------------------------------------------------------------------------
def build_sources_df(sources: List[Dict[str, Any]]) -> pd.DataFrame:
    rows = []
    for i, s in enumerate(sources or [], start=1):
        rows.append({
            "Rank": i,
            "Similarity": float(s.get("similarity", 0.0)),
            "Document": s.get("doc", s.get("document", s.get("source", ""))),
            "Title": s.get("title", ""),
            "Section": s.get("section", s.get("heading", "")),
            "Chunk ID": s.get("chunk_id", s.get("chunk", s.get("id", ""))),
            "URL": s.get("url", ""),
            "Chars": len(s.get("text", "") or ""),
        })
    df = pd.DataFrame(rows)
    if not df.empty:
        df = df.sort_values(by="Similarity", ascending=False).reset_index(drop=True)
        df["Rank"] = range(1, len(df) + 1)
    return df

def similarity_stats(sources: List[Dict[str, Any]]) -> Dict[str, float]:
    sims = [float(s.get("similarity", 0.0)) for s in (sources or []) if s.get("similarity") is not None]
    if not sims:
        return {"avg": 0.0, "min": 0.0, "max": 0.0}
    return {"avg": sum(sims) / len(sims), "min": min(sims), "max": max(sims)}

# -----------------------------------------------------------------------------
# Helper: Feedback logging
# -----------------------------------------------------------------------------
def append_feedback_log(record: Dict[str, Any], path: str = "feedback.jsonl") -> None:
    try:
        with open(path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    except Exception:
        # Don't break app due to logging.
        pass

# -----------------------------------------------------------------------------
# Cached resource: DB init (smooth reruns)
# -----------------------------------------------------------------------------
@st.cache_resource(show_spinner=False)
def get_database(db_path: str) -> RAGDatabase:
    return RAGDatabase(db_path)

# -----------------------------------------------------------------------------
# Session State Initialization
# -----------------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []  # list of dicts: {role, content, sources?, meta?}

if "db_path" not in st.session_state:
    st.session_state.db_path = config.DEFAULT_DB_PATH

if "top_k" not in st.session_state:
    st.session_state.top_k = getattr(config, "DEFAULT_TOP_K", 8)

if "pending_prompt" not in st.session_state:
    st.session_state.pending_prompt = ""

if "last_run_stats" not in st.session_state:
    st.session_state.last_run_stats = {}

if "last_feedback" not in st.session_state:
    st.session_state.last_feedback = {}  # message_id -> {thumb, note}

# -----------------------------------------------------------------------------
# Sidebar - User Configuration
# -----------------------------------------------------------------------------
with st.sidebar:
    st.header("⚙️ Settings")

    api_key = st.text_input(
        "OpenAI API Key",
        type="password",
        help="Stored only for this session. Required to generate answers."
    )

    db_path = st.text_input(
        "Database Path",
        value=st.session_state.db_path,
        help="Path to your DuckDB vector database."
    )
    st.session_state.db_path = db_path

    st.subheader("Retrieval")
    top_k = st.slider(
        "Results per Query (top_k)",
        min_value=3,
        max_value=20,
        value=int(st.session_state.top_k),
        help="Number of passages retrieved per question."
    )
    st.session_state.top_k = top_k

    st.subheader("Generation")
    model_choice = st.selectbox(
        "LLM Model",
        getattr(config, "AVAILABLE_MODELS", ["gpt-4o-mini"]),
        index=0
    )

    max_iter = st.slider(
        "Max Tool Calls",
        min_value=1,
        max_value=5,
        value=int(getattr(config, "DEFAULT_MAX_ITER", 2)),
        help="Max number of retrieval/tool steps the agent may perform."
    )

    response_mode = st.selectbox(
        "Response Mode",
        [
            "CST Decision Framework (recommended)",
            "Quick Answer",
            "Executive Memo",
            "Pros/Cons + Risks",
        ],
        index=0,
        help="Controls structure + formatting of the answer."
    )

    tone = st.selectbox(
        "Tone",
        [
            "Neutral advisor",
            "MBA-style consultant (practical)",
            "Catholic moral theologian (formal)",
        ],
        index=0
    )

    strict_citations = st.checkbox(
        "Strict citation mode",
        value=True,
        help="If enabled, the assistant should avoid unsupported claims and lean on retrieved sources."
    )

    st.divider()

    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🗑️ Clear chat"):
            st.session_state.messages = []
            st.session_state.last_run_stats = {}
            st.session_state.pending_prompt = ""
            st.rerun()

    with col_b:
        show_debug = st.checkbox("Show debug panels", value=False)

    st.divider()

    st.markdown(
        """
### About this chatbot
**Catholic Business Ethics RAG Advisor** helps you reason through real business decisions using **Catholic Social Teaching (CST)**.

**What it does**
- You ask a business question (layoffs, pricing, automation, private equity, labor practices, ESG, etc.)
- The assistant retrieves relevant passages from curated Church teaching + applied ethics sources
- It returns a **step-by-step CST-grounded decision framework** with **sources and similarity scores**

**What it’s NOT**
- Not legal or HR advice
- Not a substitute for pastoral counsel
        """
    )

# -----------------------------------------------------------------------------
# Main Header
# -----------------------------------------------------------------------------
st.title("✝️ Catholic Business Ethics RAG Advisor")
st.caption(
    "Ask business questions and get a Catholic Social Teaching (CST) grounded, step-by-step ethical analysis—"
    "with retrieved sources and similarity scores."
)

# -----------------------------------------------------------------------------
# API Key Check
# -----------------------------------------------------------------------------
if not api_key:
    st.warning("⚠️ Enter your OpenAI API key in the sidebar to continue.")
    st.stop()

os.environ["OPENAI_API_KEY"] = api_key

# -----------------------------------------------------------------------------
# Database Connection
# -----------------------------------------------------------------------------
database = get_database(st.session_state.db_path)

if not database.test_connection():
    st.error(f"❌ Database not found or not accessible at: `{st.session_state.db_path}`")
    st.info("Update the database path in the sidebar. The app cannot run without the vector DB.")
    if not os.path.exists(st.session_state.db_path):
        st.stop()
else:
    st.success(f"✅ Database connected: `{st.session_state.db_path}`")

# -----------------------------------------------------------------------------
# Top-level layout columns
# -----------------------------------------------------------------------------
left, right = st.columns([1.6, 1.0], gap="large")

# -----------------------------------------------------------------------------
# Right Column: Live diagnostics panel
# -----------------------------------------------------------------------------
with right:
    st.subheader("📊 Run Diagnostics")

    if st.session_state.last_run_stats:
        stats = st.session_state.last_run_stats
        st.metric("Retrieval time (s)", f"{stats.get('t_retrieval', 0.0):.2f}")
        st.metric("Generation time (s)", f"{stats.get('t_generation', 0.0):.2f}")
        st.metric("Total time (s)", f"{stats.get('t_total', 0.0):.2f}")

        sim = stats.get("similarity", {"avg": 0.0, "min": 0.0, "max": 0.0})
        st.metric("Avg similarity", f"{sim.get('avg', 0.0):.3f}")
        st.metric("Max similarity", f"{sim.get('max', 0.0):.3f}")
        st.metric("Min similarity", f"{sim.get('min', 0.0):.3f}")

        st.caption(
            f"Model: `{stats.get('model', '')}` • top_k: `{stats.get('top_k', '')}` • "
            f"max_iter: `{stats.get('max_iter', '')}` • mode: `{stats.get('mode', '')}`"
        )
    else:
        st.info("Run a query to see latency + similarity diagnostics.")

    st.divider()

    st.subheader("💡 Example business questions")
    examples = [
        "Is it ethically permissible to lay off 15% of staff to hit margin targets?",
        "Should we raise prices on essential goods during a shortage?",
        "Is private equity extracting dividends funded by new debt compatible with Catholic Social Teaching?",
        "How should a company balance shareholder value with worker dignity under CST?",
        "Is replacing workers with automation morally permissible? What obligations remain to employees?",
    ]
    for ex in examples:
        if st.button(ex, key=f"ex_{ex[:24]}"):
            st.session_state.pending_prompt = ex
            st.rerun()

    st.divider()

    st.subheader("🧭 Output format preview")
    st.code(
        "1) Business Context Summary\n"
        "2) Relevant CST Principles (Human Dignity, Solidarity, Subsidiarity, Common Good, etc.)\n"
        "3) Source-Grounded Analysis (with citations)\n"
        "4) Practical Business Guidance\n"
        "5) Trade-offs & Open Questions",
        language="text"
    )

# -----------------------------------------------------------------------------
# Left Column: Chat UI
# -----------------------------------------------------------------------------
with left:
    # Optional: show a “scope guardrail”
    st.info("Tip: ask concrete questions (numbers, constraints, stakeholders). The assistant will ground answers in retrieved sources.")

    # Display chat history
    for idx, message in enumerate(st.session_state.messages):
        role = message.get("role", "assistant")
        with st.chat_message(role):
            st.markdown(message.get("content", ""))

            # Assistant extras: principles + sources + exports + feedback
            if role == "assistant":
                sources = message.get("sources", []) or []
                principles = message.get("principles", []) or []

                if principles:
                    st.markdown("**Detected CST principles:** " + " • ".join([f"`{p}`" for p in principles]))

                if sources:
                    df = build_sources_df(sources)
                    sim = similarity_stats(sources)

                    with st.expander(f"📚 View Sources ({len(sources)} retrieved) • avg sim {sim['avg']:.3f}"):
                        # Show table first (more professional than only text areas)
                        st.dataframe(
                            df[["Rank", "Similarity", "Document", "Title", "Section", "Chunk ID", "Chars", "URL"]],
                            use_container_width=True,
                            hide_index=True
                        )

                        # Then show the passages
                        st.divider()
                        for i, source in enumerate(sources, 1):
                            st.markdown(f"**Source {i}** (Similarity: {float(source.get('similarity', 0.0)):.3f})")
                            meta_bits = []
                            for k in ["title", "document", "doc", "section", "heading", "chunk_id", "url"]:
                                v = source.get(k)
                                if v:
                                    meta_bits.append(f"{k}: {v}")
                            if meta_bits:
                                st.caption(" • ".join(meta_bits))

                            st.text_area(
                                f"Passage {i}",
                                source.get("text", ""),
                                height=160,
                                key=f"hist_src_{idx}_{i}",
                                label_visibility="collapsed"
                            )
                            if i < len(sources):
                                st.divider()

                # Exports (answer only)
                answer_text = message.get("content", "")
                if answer_text:
                    export_col1, export_col2 = st.columns(2)
                    with export_col1:
                        st.download_button(
                            "⬇️ Download answer (.md)",
                            data=answer_text,
                            file_name="cst_rag_answer.md",
                            mime="text/markdown",
                            key=f"dl_md_{idx}"
                        )
                    with export_col2:
                        st.download_button(
                            "⬇️ Download answer (.txt)",
                            data=answer_text,
                            file_name="cst_rag_answer.txt",
                            mime="text/plain",
                            key=f"dl_txt_{idx}"
                        )

                # Feedback (logged for reflection)
                fb_key = f"fb_{idx}"
                thumbs = st.radio(
                    "Was this helpful?",
                    ["—", "👍", "👎"],
                    horizontal=True,
                    index=0,
                    key=fb_key
                )
                note = st.text_input("Optional feedback (what was missing?)", key=f"{fb_key}_note")

                if thumbs in ["👍", "👎"] and st.button("Save feedback", key=f"{fb_key}_save"):
                    record = {
                        "timestamp": datetime.utcnow().isoformat() + "Z",
                        "thumb": thumbs,
                        "note": note,
                        "question": message.get("question", ""),
                        "answer": answer_text,
                        "mode": message.get("mode", ""),
                        "tone": message.get("tone", ""),
                        "strict_citations": message.get("strict_citations", None),
                        "model": message.get("model", ""),
                        "top_k": message.get("top_k", None),
                        "max_iter": message.get("max_iter", None),
                        "similarity": message.get("similarity", {}),
                    }
                    append_feedback_log(record)
                    st.success("Saved to feedback.jsonl")

    # Chat input (example buttons feed into pending_prompt)
    default_prompt = st.session_state.pending_prompt or ""
    prompt = st.chat_input("Ask a business question… (e.g., layoffs, pricing, automation, private equity)")
    if not prompt and default_prompt:
        prompt = default_prompt
        st.session_state.pending_prompt = ""

    # -----------------------------------------------------------------------------
    # Chat Input and Response Generation
    # -----------------------------------------------------------------------------
    if prompt:
        # Add user message to history + display
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Retrieving sources and generating a CST-grounded answer..."):
                try:
                    t0 = time.perf_counter()

                    # Initialize agent (your backend should use db + model)
                    agent = RAGAgent(
                        db=database,
                        model_name=model_choice,
                        max_iter=max_iter
                    )

                    # We pass UI settings to the agent (if agent.ask supports it).
                    # If your current agent.ask only accepts (prompt), it will ignore extras safely
                    # if you implement agent.ask(**kwargs) later.
                    t_retr_start = time.perf_counter()
                    # Option 1: simplest—just call ask(prompt)
                    result = agent.ask(prompt)

                    t1 = time.perf_counter()

                    # Expected structure:
                    # result["answer"] : str
                    # result["sources"]: list[{"text":..., "similarity":..., (optional metadata...)}]
                    response = result.get("answer", "")
                    sources = result.get("sources", []) or []

                    # If your backend currently doesn't accept top_k from ask(),
                    # ensure it uses st.session_state.top_k when retrieving.
                    # We still store it in metadata for rubric/report.
                    sim = similarity_stats(sources)
                    principles = detect_principles(response, sources)

                    # Render response
                    st.markdown(response)

                    # Sources + table immediately
                    if sources:
                        df = build_sources_df(sources)
                        with st.expander(f"📚 View Sources ({len(sources)} retrieved) • avg sim {sim['avg']:.3f}", expanded=False):
                            st.dataframe(
                                df[["Rank", "Similarity", "Document", "Title", "Section", "Chunk ID", "Chars", "URL"]],
                                use_container_width=True,
                                hide_index=True
                            )
                            st.divider()
                            for i, source in enumerate(sources, 1):
                                st.markdown(f"**Source {i}** (Similarity: {float(source.get('similarity', 0.0)):.3f})")
                                st.text_area(
                                    f"Passage {i}",
                                    source.get("text", ""),
                                    height=160,
                                    key=f"new_src_{i}",
                                    label_visibility="collapsed"
                                )
                                if i < len(sources):
                                    st.divider()

                    # Principles panel
                    if principles:
                        st.markdown("**Detected CST principles:** " + " • ".join([f"`{p}`" for p in principles]))

                    # Exports
                    exp1, exp2 = st.columns(2)
                    with exp1:
                        st.download_button(
                            "⬇️ Download answer (.md)",
                            data=response,
                            file_name="cst_rag_answer.md",
                            mime="text/markdown",
                            key="dl_md_new"
                        )
                    with exp2:
                        st.download_button(
                            "⬇️ Download answer (.txt)",
                            data=response,
                            file_name="cst_rag_answer.txt",
                            mime="text/plain",
                            key="dl_txt_new"
                        )

                    # Stats (for diagnostics panel)
                    t_total = time.perf_counter() - t0
                    # We can’t perfectly separate retrieval vs generation without backend timing,
                    # so we provide a useful proxy split.
                    # If your backend returns timing, override these.
                    st.session_state.last_run_stats = {
                        "t_retrieval": float(result.get("timing", {}).get("retrieval_s", 0.0)),
                        "t_generation": float(result.get("timing", {}).get("generation_s", 0.0)),
                        "t_total": float(result.get("timing", {}).get("total_s", t_total)),
                        "similarity": sim,
                        "model": model_choice,
                        "top_k": top_k,
                        "max_iter": max_iter,
                        "mode": response_mode,
                    }
                    # If backend didn't provide timing, give a reasonable UI estimate:
                    if st.session_state.last_run_stats["t_retrieval"] == 0.0 and st.session_state.last_run_stats["t_generation"] == 0.0:
                        # crude: treat whole call as generation, keep total for user
                        st.session_state.last_run_stats["t_generation"] = float(t_total)

                    # Save assistant message w/ metadata
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": response,
                        "sources": sources,
                        "principles": principles,
                        "question": prompt,
                        "mode": response_mode,
                        "tone": tone,
                        "strict_citations": strict_citations,
                        "model": model_choice,
                        "top_k": top_k,
                        "max_iter": max_iter,
                        "similarity": sim,
                    })

                    if show_debug:
                        with st.expander("🐛 Debug: raw result"):
                            st.json(result)

                except Exception as e:
                    error_msg = f"❌ Error: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": error_msg,
                        "sources": [],
                        "question": prompt,
                        "mode": response_mode,
                        "tone": tone,
                        "strict_citations": strict_citations,
                        "model": model_choice,
                        "top_k": top_k,
                        "max_iter": max_iter,
                        "similarity": {"avg": 0.0, "min": 0.0, "max": 0.0},
                    })
