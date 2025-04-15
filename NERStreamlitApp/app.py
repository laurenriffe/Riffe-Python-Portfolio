import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
from spacy import displacy
import pandas as pd
import json
from io import StringIO

# Set up Streamlit config
st.set_page_config(page_title="🌸 Custom NER App", layout="wide", page_icon="🧠")

# Add cute theme CSS
st.markdown("""
<style>
body {
    background-color: #ffe6f0;
}
h1, h2, h3, .stMarkdown { color: #880e4f; font-family: 'Arial Rounded MT Bold', sans-serif; }
.stButton > button {
    background-color: #f06292;
    color: white;
    border-radius: 10px;
    padding: 0.5rem 1.2rem;
    font-weight: bold;
}
.stTextInput > div > input, .stTextArea > div > textarea {
    background-color: #fff0f5;
    color: #4a148c;
    border: 1px solid #f8bbd0;
}
.sidebar .sidebar-content {
    background-color: #f8bbd0;
}
</style>
""", unsafe_allow_html=True)

# Title and instructions
st.title("🧠💖 Named Entity Recognition (NER) With Sparkle")
st.markdown("""
Welcome to your **interactive, fabulous NER app**! ✨  
Upload or paste your text 📄  
Define beautiful custom patterns 💡  
See your entities pop 💅  
Export results to impress your professor 📊  
""")

# Load spaCy model
@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

nlp = load_model()

# Session state for storing patterns
if "custom_patterns" not in st.session_state:
    st.session_state.custom_patterns = []

# Sidebar for custom entity input
st.sidebar.header("✨ Define Custom Entity Patterns")

with st.sidebar.form("pattern_form"):
    label = st.text_input("💬 Entity Label (e.g., FOOD, CELEB):")
    pattern_text = st.text_input("💬 Phrase to Match (e.g., pumpkin spice latte):")
    submitted = st.form_submit_button("➕ Add Pattern")

    if submitted and label and pattern_text:
        token_list = [{"LOWER": token.lower()} for token in pattern_text.strip().split()]
        new_pattern = {"label": label.upper(), "pattern": token_list}
        st.session_state.custom_patterns.append(new_pattern)
        st.sidebar.success(f"Added pattern for label '{label.upper()}'")

# Optional: View current patterns
if st.sidebar.checkbox("📋 Show Current Patterns"):
    st.sidebar.json(st.session_state.custom_patterns)

# Add patterns to spaCy pipeline
ruler = EntityRuler(nlp, overwrite_ents=True)
ruler.add_patterns(st.session_state.custom_patterns)

# Remove existing custom ruler if any
if "custom_ruler" in nlp.pipe_names:
    nlp.remove_pipe("custom_ruler")

# Add safely depending on whether 'ner' exists
if "ner" in nlp.pipe_names:
    nlp.add_pipe(ruler, before="ner", name="custom_ruler")
else:
    nlp.add_pipe(ruler, name="custom_ruler")

# Input section
st.subheader("📜 Input Your Text")
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("Upload a text file (e.g., .txt)", type=["txt"])

with col2:
    manual_text = st.text_area("Or paste your text here:", height=200)

text = ""
if uploaded_file is not None:
    text = StringIO(uploaded_file.getvalue().decode("utf-8")).read()
elif manual_text:
    text = manual_text

# Run NER
if st.button("✨ Run Entity Recognition") and text:
    doc = nlp(text)

    st.subheader("🎯 Recognized Entities (NER Results)")
    html = displacy.render(doc, style="ent")
    st.markdown(f"<div style='background-color:#ffe6f0; padding:15px; border-radius:12px'>{html}</div>", unsafe_allow_html=True)

    if doc.ents:
        data = [{
            "Entity Text": ent.text,
            "Label": ent.label_,
            "Start Pos": ent.start_char,
            "End Pos": ent.end_char,
            "Context": text[max(ent.start_char - 20, 0):ent.end_char + 20]
        } for ent in doc.ents]

        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
        st.download_button("⬇️ Download as CSV", df.to_csv(index=False), "entities.csv", "text/csv")
    else:
        st.warning("Hmm... no entities were found! Try different patterns or text ✨")

else:
    st.info("Upload or paste your text, then click 'Run Entity Recognition'.")

# Instructions
st.markdown("""
---
### 💬 How to Use This App
**Example:**
- Label: `FOOD`  
- Pattern: `pumpkin spice latte`

**Try this text:**
> I grabbed a pumpkin spice latte before going to the Taylor Swift concert. Best day ever!

### 🌟 Tips
- Labels are case-insensitive
- Phrases are split by spaces into token patterns
- Use emojis, slang, brand names – go wild 💅
""")

st.markdown("---")
st.caption("Made with 💖 using spaCy + Streamlit | Portfolio Project")
