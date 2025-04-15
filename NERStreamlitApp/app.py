import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
from spacy import displacy
import json
from io import StringIO
import pandas as pd

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

🌟 *This app is powered by spaCy, Streamlit, and a lot of love.*
""")

# 🌼 Load spaCy model with caching for performance
@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

nlp = load_model()

# 💖 Sidebar pattern editor with input fields
st.sidebar.header("✨ Define Custom Entity Patterns")

# Custom entity label input box
custom_label = st.sidebar.text_input("💬 Enter the Entity Label (e.g., FOOD, CELEB, etc.):", "")

# Custom pattern input box (one pattern at a time)
custom_pattern = st.sidebar.text_input("💬 Enter the Pattern (e.g., 'pumpkin spice latte'):", "")

# Add pattern button
add_custom_pattern_button = st.sidebar.button("➕ Add Custom Pattern")

# Reset custom patterns button
clear_patterns = st.sidebar.button("🗑️ Clear Custom Patterns")

# Example JSON preview (to guide users)
example_pattern = [
    {"label": "FOOD", "pattern": [{"LOWER": "pumpkin"}, {"LOWER": "spice"}, {"LOWER": "latte"}]},
    {"label": "CELEB", "pattern": [{"LOWER": "taylor"}, {"LOWER": "swift"}]},
    {"label": "EVENT", "pattern": [{"LOWER": "swift"}, {"LOWER": "concert"}]},
    {"label": "EMOTION", "pattern": [{"LOWER": "best"}, {"LOWER": "day"}, {"LOWER": "ever"}]}
]

st.sidebar.markdown("**Example Pattern JSON (for reference):**")
st.sidebar.json(example_pattern)

# 🌟 Apply custom patterns using EntityRuler if button is clicked
if add_custom_pattern_button and custom_label and custom_pattern:
    try:
        # Convert the input pattern to spaCy format
        pattern = [{"LOWER": token} for token in custom_pattern.split()]
        custom_pattern_dict = {"label": custom_label, "pattern": pattern}

        # Add custom pattern to EntityRuler
        ruler = EntityRuler(nlp, overwrite_ents=True)
        ruler.add_patterns([custom_pattern_dict])

        # Remove old ruler if it exists and add new one
        if "custom_ruler" in nlp.pipe_names:
            nlp.remove_pipe("custom_ruler")
        nlp.add_pipe(ruler, before="ner", name="custom_ruler")

        st.sidebar.success(f"🎉 Custom pattern '{custom_label}' added successfully!")

    except Exception as e:
        st.sidebar.error(f"❌ Error: {e}")

# Clear custom patterns
if clear_patterns:
    if "custom_ruler" in nlp.pipe_names:
        nlp.remove_pipe("custom_ruler")
    st.sidebar.success("🎉 Custom patterns cleared!")

# 📄 Text input section
st.subheader("📜 Input Your Text")
col1, col2 = st.columns([1, 1])

# Upload file or paste text
with col1:
    uploaded_file = st.file_uploader("Upload a text file (e.g., .txt)", type=["txt"])

with col2:
    manual_text = st.text_area("Or paste your text here:", height=200)

# Read uploaded or typed text
text = ""
if uploaded_file is not None:
    text = StringIO(uploaded_file.getvalue().decode("utf-8")).read()
elif manual_text:
    text = manual_text

# 🔍 Process NER
if st.button("✨ Run Entity Recognition") and text:
    doc = nlp.make_doc(text)
    if "custom_ruler" in nlp.pipe_names:
        doc = nlp.get_pipe("custom_ruler")(doc)
    doc = nlp.get_pipe("ner")(doc)

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
