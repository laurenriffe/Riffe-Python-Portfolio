import streamlit as st
import spacy
from spacy import displacy
from spacy.language import Language
import pandas as pd
from io import StringIO

# Streamlit app config
st.set_page_config(page_title="🌸 Custom NER App", layout="wide", page_icon="🧠")

# Custom CSS
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

st.title("🧠💖 Named Entity Recognition (NER) With Sparkle")
st.markdown("""
Welcome to your **interactive, fabulous NER app**! ✨  
Upload or paste your text 📄  
Define beautiful custom patterns 💡  
See your entities pop 💅  
Export results to impress your professor 📊  
""")

@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

nlp = load_model()

# Clear existing custom_ruler if needed
if "custom_ruler" in nlp.pipe_names:
    nlp.remove_pipe("custom_ruler")

# Add new entity ruler
if "ner" in nlp.pipe_names:
    ruler = nlp.add_pipe("entity_ruler", config={"overwrite_ents": True}, before="ner", name="custom_ruler")
else:
    ruler = nlp.add_pipe("entity_ruler", config={"overwrite_ents": True}, name="custom_ruler")

# Sidebar for custom patterns
st.sidebar.header("✨ Define Custom Entity Patterns")
if "custom_patterns" not in st.session_state:
    st.session_state.custom_patterns = []

with st.sidebar.form("add_pattern_form"):
    label = st.text_input("💬 Entity Label (e.g. FOOD, CELEB)")
    phrase = st.text_input("💬 Phrase to Match (e.g. pumpkin spice latte)")
    add = st.form_submit_button("➕ Add Pattern")
    if add and label and phrase:
        pattern = [{"LOWER": word.lower()} for word in phrase.strip().split()]
        st.session_state.custom_patterns.append({"label": label.upper(), "pattern": pattern})
        st.sidebar.success(f"Added pattern for {label.upper()}: '{phrase}'")

if st.sidebar.checkbox("📋 Show Current Patterns"):
    st.sidebar.json(st.session_state.custom_patterns)

# Add patterns to ruler
ruler.add_patterns(st.session_state.custom_patterns)

# Text input
st.subheader("📜 Input Your Text")
col1, col2 = st.columns(2)
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
    st.subheader("🎯 Recognized Entities (NER Results)")
    html = displacy.render(doc, style="ent")
    st.markdown(f"<div style='background-color:#ffe6f0; padding:15px; border-radius:12px'>{html}</div>", unsafe_allow_html=True)

    if doc.ents:
        data = [{
            "Entity Text": ent.text,
            "Label": ent.label_,
            "Start": ent.start_char,
            "End": ent.end_char,
            "Context": text[max(ent.start_char-20,0):ent.end_char+20]
        } for ent in doc.ents]
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
        st.download_button("⬇️ Download CSV", df.to_csv(index=False), "entities.csv", "text/csv")
    else:
        st.warning("Hmm... no entities found! Try different patterns or text ✨")
else:
    st.info("Upload or paste your text, then click 'Run Entity Recognition'.")

# Help Section
st.markdown("""
---
### 💬 How to Use This App
- **Label**: What kind of thing it is (e.g., `FOOD`, `CELEB`)
- **Phrase**: The exact words to match (e.g., `pumpkin spice latte`)

**Example input text:**  
> I grabbed a pumpkin spice latte before going to the Taylor Swift concert. Best day ever!

---
#### 💖 Built with spaCy + Streamlit
""")
