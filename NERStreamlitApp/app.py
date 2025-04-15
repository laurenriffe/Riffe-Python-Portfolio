import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
from spacy import displacy
import json
from io import StringIO
import pandas as pd

# 🌸 Set up Streamlit page config
st.set_page_config(page_title="🌸 Custom NER App", layout="wide", page_icon="🧠")

# 🎀 Style
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

st.title("🧠💖 Named Entity Recognition (NER) With Sparkle")

# Load base model
@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

nlp = load_model()

# Store custom patterns in session
if "custom_patterns" not in st.session_state:
    st.session_state.custom_patterns = []

# Sidebar Inputs
st.sidebar.header("✨ Add Custom Entity Pattern")
label = st.sidebar.text_input("Label (e.g. CELEB, FOOD):")
phrase = st.sidebar.text_input("Pattern Phrase (e.g. pumpkin spice latte)")

if st.sidebar.button("➕ Add Pattern"):
    if label and phrase:
        pattern = {"label": label, "pattern": [{"LOWER": word} for word in phrase.split()]}
        st.session_state.custom_patterns.append(pattern)
        st.sidebar.success("Pattern added!")

if st.sidebar.button("🗑️ Clear Patterns"):
    st.session_state.custom_patterns = []
    st.sidebar.success("Patterns cleared.")

# Create and add EntityRuler with all stored patterns
ruler = EntityRuler(nlp, overwrite_ents=True)
ruler.add_patterns(st.session_state.custom_patterns)

# Remove and re-add to pipeline cleanly
if "custom_ruler" in nlp.pipe_names:
    nlp.remove_pipe("custom_ruler")
nlp.add_pipe(ruler, before="ner", name="custom_ruler")

# Input Text Area
st.subheader("📜 Input Your Text")
col1, col2 = st.columns([1, 1])

with col1:
    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
with col2:
    manual_text = st.text_area("Or paste your text here:", height=200)

text = ""
if uploaded_file:
    text = StringIO(uploaded_file.getvalue().decode("utf-8")).read()
elif manual_text:
    text = manual_text

# Run NER
if st.button("✨ Run Entity Recognition") and text:
    doc = nlp(text)

    # Display entities
    st.subheader("🎯 Recognized Entities")
    html = displacy.render(doc, style="ent")
    st.markdown(f"<div style='background-color:#ffe6f0; padding:15px; border-radius:12px'>{html}</div>", unsafe_allow_html=True)

    if doc.ents:
        st.subheader("📊 Entity Table")
        df = pd.DataFrame([{
            "Entity Text": ent.text,
            "Label": ent.label_,
            "Start Pos": ent.start_char,
            "End Pos": ent.end_char,
            "Context": text[max(ent.start_char - 20, 0):ent.end_char + 20]
        } for ent in doc.ents])
        st.dataframe(df)
        st.download_button("⬇️ Download as CSV", df.to_csv(index=False), "entities.csv", "text/csv")
    else:
        st.warning("No entities found 😕 Try adding more patterns or a different input.")
else:
    st.info("Upload or paste your text, then click 'Run Entity Recognition'.")
