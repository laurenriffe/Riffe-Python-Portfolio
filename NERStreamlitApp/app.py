import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
from spacy import displacy
import pandas as pd
from io import StringIO
import json

# 🌸 Set up Streamlit page config
st.set_page_config(page_title="🌸 Custom NER App", layout="wide", page_icon="🧠")

# 🌷 Background style with pink theme
st.markdown("""
<style>
body {
    background-color: #ffe6f0;
    font-family: 'Comic Sans MS', cursive, sans-serif;
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

# 🌟 Title and description
st.title("🧠💖 Named Entity Recognition (NER) With Sparkle")
st.markdown("""
Welcome to your **interactive, fabulous NER app**! ✨ 

- Upload or paste your own text 📄  
- Define beautiful custom patterns using spaCy's EntityRuler 💡  
- See your entities pop in a lovely visualization 💅  
- Export your work to impress your professor 📊  
""")

# Load spaCy model
@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

nlp = load_model()

# Store custom patterns in session
if "custom_patterns" not in st.session_state:
    st.session_state.custom_patterns = []

# 💖 Sidebar pattern editor
st.sidebar.header("✨ Define Custom Entity Patterns")
label = st.sidebar.text_input("💬 Enter the Entity Label (e.g., FOOD, CELEB, etc.):")
phrase = st.sidebar.text_input("💬 Enter the Pattern (e.g., pumpkin spice latte):")

if st.sidebar.button("➕ Add Pattern"):
    if label and phrase:
        try:
            pattern = {
                "label": label.strip().upper(),
                "pattern": [{"LOWER": word} for word in phrase.strip().split()]
            }
            st.session_state.custom_patterns.append(pattern)
            st.sidebar.success("✅ Pattern added!")
        except Exception as e:
            st.sidebar.error(f"❌ Error: {e}")
    else:
        st.sidebar.warning("⚠️ Please fill in both the label and pattern!")

# Show current patterns
if st.session_state.custom_patterns:
    st.sidebar.markdown("### 📋 Current Patterns")
    st.sidebar.json(st.session_state.custom_patterns)

# Build EntityRuler with current patterns
ruler = EntityRuler(nlp, overwrite_ents=True)
ruler.add_patterns(st.session_state.custom_patterns)

# Remove old pipe and add updated one
if "custom_ruler" in nlp.pipe_names:
    nlp.remove_pipe("custom_ruler")

if "ner" in nlp.pipe_names:
    nlp.add_pipe(ruler, before="ner", name="custom_ruler")
else:
    nlp.add_pipe(ruler, name="custom_ruler")

# 📄 Text input section
st.subheader("📜 Input Your Text")
col1, col2 = st.columns([1, 1])

with col1:
    uploaded_file = st.file_uploader("Upload a text file (e.g., .txt)", type=["txt"])

with col2:
    manual_text = st.text_area("Or paste your text here:", height=200)

# Get final text
text = ""
if uploaded_file is not None:
    text = StringIO(uploaded_file.getvalue().decode("utf-8")).read()
elif manual_text:
    text = manual_text

# 🔍 Process NER
if st.button("✨ Run Entity Recognition") and text:
    doc = nlp(text)

    st.subheader("🎯 Recognized Entities (NER Results)")

    # 🔮 Display entities with displacy
    html = displacy.render(doc, style="ent")
    st.markdown(f"<div style='background-color:#ffe6f0; padding:15px; border-radius:12px'>{html}</div>", unsafe_allow_html=True)

    # 📊 Show entity table
    if doc.ents:
        st.subheader("📊 Entity Table with Details")
        data = [{
            "Entity Text": ent.text,
            "Label": ent.label_,
            "Start Pos": ent.start_char,
            "End Pos": ent.end_char,
            "Context": text[max(ent.start_char - 20, 0):ent.end_char + 20]
        } for ent in doc.ents]

        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)

        # Allow download
        st.download_button("⬇️ Download as CSV", df.to_csv(index=False), "entities.csv", "text/csv")
    else:
        st.warning("Hmm... no entities were found! Try different patterns or text ✨")
else:
    st.info("Upload or paste your text, then click 'Run Entity Recognition'.")


