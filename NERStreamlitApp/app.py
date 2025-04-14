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

# 💖 Sidebar pattern editor
st.sidebar.header("✨ Define Custom Entity Patterns")
st.sidebar.markdown("Add your spaCy-compatible patterns in JSON format!")

example_pattern = [
    {"label": "FOOD", "pattern": [{"LOWER": "pumpkin"}, {"LOWER": "spice"}, {"LOWER": "latte"}]},
    {"label": "CELEB", "pattern": [{"LOWER": "taylor"}, {"LOWER": "swift"}]},
    {"label": "EVENT", "pattern": [{"LOWER": "swift"}, {"LOWER": "concert"}]},
    {"label": "EMOTION", "pattern": [{"LOWER": "best"}, {"LOWER": "day"}, {"LOWER": "ever"}]}
]

# Provide editable text area with JSON examples
pattern_input = st.sidebar.text_area(
    "💡 Pattern JSON Input:",
    value=json.dumps(example_pattern, indent=2),
    height=250
)

# Button to apply patterns
add_patterns = st.sidebar.button("➕ Add Custom Patterns")

# 🌟 Apply patterns using spaCy's EntityRuler
if add_patterns:
    try:
        patterns = json.loads(pattern_input)
        ruler = EntityRuler(nlp, overwrite_ents=True)
        ruler.add_patterns(patterns)
        if "custom_ruler" in nlp.pipe_names:
            nlp.remove_pipe("custom_ruler")
        nlp.add_pipe(ruler, before="ner", name="custom_ruler")
        st.sidebar.success("🎉 Custom patterns added successfully!")
    except Exception as e:
        st.sidebar.error(f"❌ Pattern error: {e}")

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

# 💬 Examples and tips for students
st.markdown("""
---
### 💬 How to Use This App
**Example pattern JSON:**
```json
[
  {"label": "FOOD", "pattern": [{"LOWER": "pumpkin"}, {"LOWER": "spice"}, {"LOWER": "latte"}]},
  {"label": "CELEB", "pattern": [{"LOWER": "taylor"}, {"LOWER": "swift"}]},
  {"label": "EVENT", "pattern": [{"LOWER": "swift"}, {"LOWER": "concert"}]},
  {"label": "EMOTION", "pattern": [{"LOWER": "best"}, {"LOWER": "day"}, {"LOWER": "ever"}]}
]
```

**Try pasting this text:**
> I grabbed a pumpkin spice latte before going to the Taylor Swift concert. Best day ever!

---
### 🌟 What Each Column Means:
- **Entity Text:** The exact phrase spaCy found
- **Label:** The type/category you assigned it (e.g., ORG, FOOD, CELEB)
- **Start/End Pos:** Where in the text the entity appears
- **Context:** Helpful nearby words so you see the entity in action

---
### 🛠️ Advanced Tips
- Patterns support token attributes like `LOWER`, `TEXT`, `IS_TITLE`
- Multi-word phrases must be in a list of dicts
- Try adding emojis, brand names, slang, or niche labels 💅

### 💖 Credits
This app was designed with flair by a fabulous developer who likes pink, clarity, and NER ✨
""")

# 🌈 Footer
st.markdown("---")
st.caption("Made with 💖 using spaCy + Streamlit | Portfolio Update #3 | Spring 2025")
