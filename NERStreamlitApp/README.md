# 💖 Named Entity Recognition (NER) App With Sparkle

Welcome to the **NER With Sparkle App** — a vibrant, emoji-rich, and interactive web application designed for Named Entity Recognition (NER) using spaCy and Streamlit. Built with customization in mind, this tool allows users to define their own entity patterns and analyze text for both pre-trained and custom labels. This app was created as a personal project to combine creativity, usability, and core natural language processing concepts in an accessible and visually engaging way.

Perfect for students, NLP beginners, or anyone who wants to make text analysis ✨fabulous✨.

---

## 🧠 Purpose & Learning Outcomes

This project is designed to:
- Demonstrate the power and flexibility of spaCy's `EntityRuler`
- Help users interactively understand how NER works by editing and viewing custom entity patterns in real time
- Provide hands-on experience with text preprocessing and recognition
- Showcase how user-friendly interfaces and branding can improve adoption and comprehension of technical tools

By the end of exploring this app, users will:
- Understand how to define rule-based entities
- Recognize key functionality of spaCy pipelines
- Feel comfortable exporting and working with NER output in CSV format

---

## 📊 Project Overview

**NER With Sparkle** is a web-based natural language processing tool that uses `spaCy` to recognize and categorize named entities in any user-provided text. It goes beyond basic NER by allowing the user to define their own custom labels and phrase patterns, which are added to spaCy’s processing pipeline using the `EntityRuler` component. The app runs entirely in-browser via Streamlit and offers live visualization and data table exports for further exploration.

This project merges:
- Pre-trained NER via `en_core_web_sm`
- Rule-based annotation for user-defined categories
- Front-end UX customizations to create a warm and accessible data tool

Use cases include:
- Teaching students how NLP models work
- Collecting data for user-defined categories (e.g., `FOOD`, `CELEBRITY`, `BRAND`)
- Reviewing or annotating written material for patterns and structure

---

## 🎯 Key Features

- 📝 **Paste or Upload Text** – Analyze long-form text or quick blurbs
- ✏️ **Custom Pattern Builder** – Define and visualize new entity categories
- 🧠 **spaCy + EntityRuler** – Integrate rule-based patterns with machine-learned NER
- 📦 **Interactive Annotations** – View highlighted entities with label color overlays
- 📊 **Dataframe Output** – Access, sort, and download entity results in table format
- 💾 **Export to CSV** – Save the full entity list and metadata with one click

---

## 🧰 Tech Stack

| Tool        | Purpose                            |
|-------------|------------------------------------|
| `Python`    | Core application logic              |
| `spaCy`     | NLP engine for NER & tokenization   |
| `Streamlit` | Interactive web interface           |
| `pandas`    | Tabular result formatting/export    |

---

## 📁 Project Directory Structure

```
NERStreamlitApp/
├── app.py                # Main application file
├── README.md             # Project documentation (this file)
```

---

## ⚙️ Setup & Launch Instructions

### 1. Clone the Repository
```
git clone https://github.com/laurenriffe/Riffe-Python-Portfolio.git
cd Riffe-Python-Portfolio/NERStreamlitApp
```

### 2. Install Required Libraries
```
pip install streamlit spacy pandas
python -m spacy download en_core_web_sm
```

### 3. Launch the App
```
streamlit run app.py
```

---

## 🧪 Example Scenario

Let’s say a user wants to find `FOOD` and `CELEB` references in this sentence:

> I grabbed a pumpkin spice latte before going to the Taylor Swift concert.

They would:
1. Upload or paste the text
2. Define two custom patterns:
   - Label: `FOOD`, Phrase: `pumpkin spice latte`
   - Label: `CELEB`, Phrase: `Taylor Swift`
3. Click **Run Entity Recognition**
4. See the terms highlighted and their metadata in a downloadable table

This tool is great for both casual exploration and early-phase annotation workflows.

---

## 📌 Requirements
- Python 3.7+
- Streamlit
- spaCy
- pandas

Install with:
```
pip install streamlit spacy pandas
python -m spacy download en_core_web_sm
```

---

## 📚 References
- [spaCy NER Documentation](https://spacy.io/usage/linguistic-features#named-entities)
- [EntityRuler API](https://spacy.io/api/entityruler)
- [Streamlit Docs](https://docs.streamlit.io/)

---

## 🌟 Why This Project Stands Out
- ✅ Combines rule-based and statistical NLP in a clean interface
- ✅ Promotes hands-on learning by letting users define their own entities
- ✅ Bridges academic NLP and playful branding for wider engagement
- ✅ Encourages experimentation while remaining technically robust

---

## 👩‍💻 About the Creator

Lauren Riffe is a Finance major at the University of Notre Dame with minors in Computing & Digital Technologies and Theology. She builds creative, user-friendly tools that blend serious functionality with joyful design — making data analysis both beautiful and empowering.

📫 [lriffe@nd.edu](mailto:lriffe@nd.edu)  
🔗 [LinkedIn](https://www.linkedin.com/in/lauren-riffe)

---
