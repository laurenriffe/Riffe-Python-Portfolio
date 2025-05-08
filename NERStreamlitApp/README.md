# ✝️ Emotional Bible Guide: A Streamlit App for Soul + Self-Care 🌈

## 🧠 Project Overview

The **Emotional Bible Guide** is a personalized, emotionally intelligent web app built to provide holistic spiritual and emotional support. Using advanced NLP (`spaCy`), structured data (`pandas`), and an elegant UI (`Streamlit`), this app helps users connect their emotional states with relevant scripture and Christian self-care practices.

> This app was designed with one goal: to care for the **whole person** — spirit, mind, and body. Because mental wellness and faith are not mutually exclusive — they’re mutually necessary.

---

## ⚙️ Setup & Run Instructions

### 📥 Installation Requirements

Make sure Python is installed (Python 3.9+ recommended).

### 🔧 Install Dependencies

```bash
pip install streamlit pandas spacy
python -m spacy download en_core_web_sm

### 📁 File Structure
StreamlitAppFinal/
│
├── bibleapp.py
├── Final_Emotional_Bible.csv
├── self_care_activities_updated.csv
├── Christian_Emotions_Interpretation_Survey_Extended.csv
├── Emotion_Quiz_Prompts.csv
├── README.md


###▶️ Run the App
From the root directory:

streamlit run bibleapp.py
Open your browser to http://localhost:8501 if it doesn’t open automatically.

### 🌟 App Features
🧭 Navigation
Switch between pages using the sidebar:

Home – Introduction and aesthetic overview
Verse Finder – Write your feelings → Get 3 Bible verses + reflection
Emotional Quiz – Not sure how you feel? Check a few boxes to get a diagnosis + self-care suggestion

### ✍️ Verse Finder
User Input: Free-text reflection
Processing: spaCy NLP extracts emotional keywords (nouns/adjectives/verbs)
Matching: Matches keywords to emotion-tagged verses in a CSV
Output: 3 verse cards with styled text, matching emotion, and custom reflections

### 🌈 Emotional Discovery Quiz
User Input: 12 checkboxes (each with a unique emoji + color)
Processing: Scores your top emotional state based on answers
Output: Suggests a glow-styled Christian self-care activity

### 🎨 Design & UX Highlights
🌸 Custom CSS glow boxes and floating headers
🌈 Animated gradients, emotive emojis, and color-coded responses
💬 Tooltips, feedback prompts, and rotating affirmations
🧩 Modular and readable code with full error handling and caching

### 📚 References & Resources
Streamlit Docs
spaCy NLP
Pandas
Design inspiration: CSS Tricks
Emojis: Emojipedia
Color Palettes: Coolors
Bible content: Curated from public-domain scripture repositories

### 🖼️ Visual Examples
<img width="621" alt="Screenshot 2025-05-07 at 10 09 15 PM" src="https://github.com/user-attachments/assets/73eedad7-3b96-4e78-ba13-e70b351b6860" />

<img width="621" alt="Screenshot 2025-05-07 at 10 09 41 PM" src="https://github.com/user-attachments/assets/3b182f32-610c-49e1-a33d-a5c2c5201678" />

### 🙌 Final Thoughts
The Emotional Bible Guide isn’t just an app — it’s a peaceful place to feel, reflect, and heal. Whether you’re experiencing spiritual highs or emotional lows, this app brings God’s word into your everyday emotional vocabulary.


