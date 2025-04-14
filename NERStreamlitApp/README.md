# 🧠 Named Entity Recognition (NER) App using spaCy + Streamlit

This project is an interactive Streamlit web app that performs Named Entity Recognition (NER) on custom text input. It lets users define their own entities using `spaCy`'s `EntityRuler`.

## 🚀 Features

- Upload or paste your own text for analysis.
- Define custom entities with labels and patterns using JSON.
- Visualize named entities with color-coded highlights.
- Uses spaCy’s NLP pipeline with optional custom rules.

## 🛠 Setup

```bash
git clone https://github.com/yourusername/NERStreamlitApp.git
cd NERStreamlitApp
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py
