# ✝️ Spiritual Guidance App
<img width="633" alt="image" src="https://github.com/user-attachments/assets/36252957-1e3f-440e-81e7-b9c20a2cdd2a" />


Welcome to the **Spiritual Guidance App**, a soulful Streamlit web app that combines natural language processing (NLP), faith-based wisdom, and visual design to help users reflect emotionally and spiritually. Whether you're overwhelmed, joyful, or unsure how you feel, this app guides you to scripture and Christian self-care practices that meet you where you are.

---

## 🧠 Purpose & Learning Outcomes 

This project is designed to:
- Help users reflect on emotional states through expressive writing or structured self-assessment
- Leverage NLP to map feelings to a labeled emotion dataset of curated Bible verses
- Encourage holistic wellness by combining spiritual encouragement with emotional awareness
- Showcase how technology can uplift and empower spiritual practice

By using this tool, users can:
- Gain insights into their emotional state
- Receive personalized biblical encouragement
- Explore Christian self-care ideas

---

## 📊 Project Overview

**The Emotional Bible Verse Reader** is an app with two main features:
<img width="1011" alt="image" src="https://github.com/user-attachments/assets/daf31fb7-191a-44c5-ba92-559993bd91f5" />

### 📖 1. Verse Finder
- Users write how they're feeling in free-form text
<img width="1003" alt="image" src="https://github.com/user-attachments/assets/a988027c-c5f3-491a-a527-dcd8fdef6f57" />

- spaCy’s NLP engine identifies emotional keywords
- Keywords are matched to a dataset of labeled Bible verses
- Users receive 3 relevant verses and a spiritual reflection
<img width="1003" alt="image" src="https://github.com/user-attachments/assets/520859bb-b228-4f82-8114-3089b07420e9" />


### 🌈 2. Relief Activity Assessment
- Users check statements that describe how they feel
<img width="1003" alt="image" src="https://github.com/user-attachments/assets/4a060bce-c289-46ee-8f62-540ea4890d72" />

- The system calculates their dominant emotion
- Personalized self-care recommendations are presented based on the emotion
<img width="1003" alt="image" src="https://github.com/user-attachments/assets/be923b67-40dc-46d6-b881-e1ce2cd38296" />


---

## 🎯 Key Features
- 💬 **Text-Based Reflection Input** – Users can describe their feelings naturally
- 🔍 **Emotion Keyword Extraction** – spaCy analyzes the text to identify core emotional terms
- 📖 **Bible Verse Matching** – Top-matching verses displayed with labeled emotion and interpretation
- 🧠 **Emotional Quiz** – Checkbox survey auto-detects dominant feeling and returns a care activity
- 🎨 **Custom UI/UX Design** – Clean, pastel-themed app with CSS animation and glowing section boxes
- 💾 **CSV-Based Datasets** – Bible verse + emotion tags, survey questions, and activity descriptions are fully editable

---

## 🧰 Tech Stack

| Tool         | Purpose                                        |
|--------------|------------------------------------------------|
| `Python`     | App logic and backend                          |
| `Streamlit`  | Front-end UI + routing                         |
| `spaCy`      | NLP engine for emotion keyword extraction      |
| `pandas`     | Data processing + CSV integration              |
| `HTML/CSS`   | Custom styling for vibrant user experience     |

---

## 📁 Project Directory Structure

```
StreamlitAppFinal/
├── bibleapp.py                              # Main Streamlit app
├── Final_Emotional_Bible.csv                # Emotion-tagged Bible verses
├── self_care_activities_updated.csv         # Activities mapped to emotions
├── Christian_Emotions_Interpretation_Survey_Extended.csv  # Relief quiz questions
├── README.md                                # This documentation file
```

---

## ⚙️ Setup Instructions (Local)

### 1. Clone the Repository
```
git clone https://github.com/laurenriffe/Riffe-Python-Portfolio.git
cd Riffe-Python-Portfolio/StreamlitAppFinal
```

### 2. Install Required Libraries
```
pip install streamlit pandas spacy
python -m spacy download en_core_web_sm
```

### 3. Run the App
```
streamlit run bibleapp.py
```

You’ll be able to use the sidebar to navigate between the **Home**, **Verse Finder**, and **Relief Activity Assessment** pages.

---

## ☁️ Deployment (Cloud)

This app can be deployed to [Streamlit Cloud](https://streamlit.io/cloud) by:
1. Uploading the repo to your GitHub account
2. Creating a new app and pointing it to `bibleapp.py`
3. Ensuring the required CSV files are included in the repo
4. Adding a `requirements.txt` with:
```
streamlit
pandas
spacy
```

---

## 🖼 Screenshots

### 🏠 Home Page with Navigation
*Clean visual entrypoint for users to begin exploring their emotions through Scripture.*

### 📖 Verse Finder (User Input Example)
*Input field, emotion extraction results, matching verses with reflection.*

### 🌈 Relief Activity Assessment
*Checkbox quiz with dynamic emotion scoring and personalized care activity.*

---

## 📌 Requirements
- Python 3.7+
- Streamlit
- spaCy (`en_core_web_sm`)
- pandas

Install with:
```
pip install streamlit pandas spacy
python -m spacy download en_core_web_sm
```

---

## 📚 References
- [spaCy Docs](https://spacy.io)
- [Streamlit Docs](https://docs.streamlit.io)
- [Custom CSS Animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animations/Using_CSS_animations)
- [Pandas Documentation](https://pandas.pydata.org/)

---

## 🌟 Why This Project Stands Out
- ✅ Fuses faith, technology, and design
- ✅ Offers a calm, uplifting space to reflect spiritually and emotionally
- ✅ Fully editable CSV-based back-end for future customization or ministry use
- ✅ Unique example of using NLP in wellness + devotional contexts

---

## 👩‍💻 About the Creator

Lauren Riffe is a Finance major at the University of Notre Dame with minors in Computing & Digital Technologies and Theology. This project reflects her mission to design emotionally intelligent tech with spiritual depth, accessible design, and practical impact.

📫 [lriffe@nd.edu](mailto:lriffe@nd.edu)  
🔗 [LinkedIn](https://www.linkedin.com/in/lauren-riffe)

---

> “God meets us where we are — this tool simply gives language and light to the journey.”
