# importing Streamlit for the app UI
import streamlit as st
# pandas to handle all the CSV/dataframe stuff
import pandas as pd
# spaCy is the NLP engine I’m using to understand emotion words
import spacy
# random just in case I want to shuffle or randomly select stuff later
import random
# os is for working with file paths so the app knows where to look
import os

# Set up the page config first
st.set_page_config(page_title="Home", layout="wide")

# THEN define your sidebar navigation menu
page = st.sidebar.radio("Navigate", ["Home", "Verse Finder", "Relief Activity Assessment"])

# Load spaCy NLP model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    st.error("Please install the spaCy model: `python -m spacy download en_core_web_sm`")
    st.stop()

# Load the Bible verse dataset
csv_path = os.path.join(os.path.dirname(__file__), "Final_Emotional_Bible.csv")
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    df['Primary Emotion'] = df['Primary Emotion'].str.lower().str.strip()
else:
    st.error(f"Bible verse CSV not found at: {csv_path}")
    st.stop()

# -------------------- HOME PAGE --------------------
if page == "Home":
    # 🎉 Big welcome title and subtitle
    st.markdown("""
    <div class='title'>Welcome to Wellness ✝️</div>
    <div class='subtitle'> For your soul and your body! 🌟</div>
    """, unsafe_allow_html=True)

    st.markdown("""
<div style='margin-top: 40px; padding: 25px; background-color: #f5eaff; border-left: 6px solid #ab47bc; border-radius: 12px; box-shadow: 0 0 15px #e1bee7aa;'>
    <h4 style='color: #5e35b1;'>🧠💖 Built to Care for the Whole You</h4>
    <p style='font-size: 16px; color: #4a235a;'>
    This app was thoughtfully designed as more than just a digital tool — it’s a faith-centered space for self-awareness, Scripture engagement, and emotional renewal. By combining <strong>natural language processing (spaCy NLP)</strong> with a custom-tagged dataset of Bible verses, the Verse Finder helps users name what they’re feeling and ground those emotions in God’s Word. 
    </p>
    <p style='font-size: 16px; color: #4a235a;'>
    Meanwhile, the Emotional Discovery Quiz blends <strong>self-reflection prompts</strong> with personalized <strong>Christian-based self-care suggestions</strong>, helping users nurture both their inner world and daily habits. At its core, this project supports mental, emotional, and spiritual wellness — a reminder that God cares deeply about the whole person. ✨ 
    </p>
</div>
""", unsafe_allow_html=True)


    # 🧭 Friendly prompt to guide the user
    st.markdown("""
    <div style='text-align: center; margin-top: 30px; font-size: 18px; color: #6a1b9a;'>
        👈 Use the sidebar to get started. We’re so glad you’re here.
    </div>
    """, unsafe_allow_html=True)
    # 🎨 Add side-by-side colorful boxes for app feature descriptions
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
    <div style='background-color: #fff0f9; padding: 20px; border-radius: 20px; border-left: 6px solid #e75480; animation: glowFade 3s ease-in-out infinite alternate;'>
        <h3 style='color: #5b2c6f;'>📖 Verse Finder</h3>
        <p style='font-size: 16px; color: #4a235a;'>
        Write how you’re feeling in your own words. Our app uses spaCy NLP to identify the emotions you’re expressing —
        then matches them with Bible verses full of love, hope, and conviction.
        </p>
    </div>
    """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
    <div style='background-color: #e0f7fa; padding: 20px; border-radius: 20px; border-left: 6px solid #26c6da; animation: glowFade 3s ease-in-out infinite alternate;'>
        <h3 style='color: #154360;'>🧠 Relief Activity Assessment </h3>
        <p style='font-size: 16px; color: #154360;'>
        Not sure what you're feeling? Check the statements that resonate with you and we’ll suggest your most likely emotion — along with a self-care activity to help you through it.
        </p>
    </div>
    """, unsafe_allow_html=True)

    
        

# adding custom CSS styles to make the app actually look good
st.markdown(""" <style>
html, body, [class*="css"] {
background: linear-gradient(to bottom right, #fef6ff, #e6ccff);  /* soft pastel bg */
color: #2e003e;  /* deep purple font color */
font-family: 'Georgia', serif;  /* elegant font choice */
animation: fadeInBody 2s ease-in;  /* fades the app in nicely */
}
.title {
text-align: center;  /* center-aligns the title */
color: #5b2c6f;  /* heading color */
font-size: 60px;  /* pretty big title */
margin-bottom: 10px;  /* spacing under the title */
animation: floatTitle 2s ease-in-out infinite alternate;  /* makes it float/vibe */
}
.subtitle {
text-align: center;  /* subtitle is centered too */
font-size: 24px;  /* smaller than title but still noticeable */
color: #8e44ad;  /* a lighter purple for contrast */
margin-bottom: 30px;  /* gives room below it */
animation: fadeIn 3s ease-in;  /* soft intro animation */
}
.description-box {
background: #fff8fc;  /* pale pink background */
padding: 25px;  /* some internal spacing */
border-radius: 20px;  /* rounded corners for softness */
border: 3px dashed #c39bd3;  /* makes it look scrapbook-y */
font-size: 17px;  /* readable but not too big */
margin-bottom: 30px;  /* space under the box */
animation: riseIn 1.5s ease-in-out;  /* the box kind of “lifts in” */
}
.step {
padding: 15px;  /* padding for each step block */
border-radius: 12px;  /* rounded steps */
font-size: 16px;  /* consistent with body text */
margin: 10px 0;  /* space between steps */
font-weight: bold;  /* so they stand out */
}
.step-1 { background-color: #ffe4ec; border-left: 6px solid #ff5c8a; }  /* pink step */
.step-2 { background-color: #e0f7fa; border-left: 6px solid #26c6da; }  /* blue step */
.step-3 { background-color: #f1f8e9; border-left: 6px solid #9ccc65; }  /* green step */
.verse-box {
background: #fff0f9;  /* light pink box for the Bible verse area */
border-left: 6px solid #e75480;
padding: 18px;
margin: 20px 0px;
border-radius: 14px;
animation: glowFade 3s ease-in-out infinite alternate;
}
.explanation-box {
background-color: #e2f0ff;
border-left: 6px solid #2980b9;
padding: 12px;
margin-top: 8px;
border-radius: 10px;
font-size: 15px;
color: #154360;
animation: slideInLeft 2s ease-out;
}
@keyframes fadeInBody {
from {opacity: 0;}
to {opacity: 1;}
}
@keyframes fadeIn {
0% {opacity: 0; transform: translateY(10px);}
100% {opacity: 1; transform: translateY(0);}
}
@keyframes floatTitle {
0% {transform: translateY(0);}
100% {transform: translateY(-10px);}
}
@keyframes riseIn {
from {transform: translateY(40px); opacity: 0;}
to {transform: translateY(0); opacity: 1;}
}
@keyframes glowFade {
from {box-shadow: 0 0 8px #ffddee;}
to {box-shadow: 0 0 24px #ff99dd;}
}
@keyframes slideInLeft {
from {opacity: 0; transform: translateX(-30px);}
to {opacity: 1; transform: translateX(0);}
} </style>
""", unsafe_allow_html=True)

# 📊 Load the emotional survey data CSV — this dataset includes descriptions and biblical interpretations for different emotions
survey_path = os.path.join(os.path.dirname(__file__), "Christian_Emotions_Interpretation_Survey_Extended.csv")  # builds a full path to the survey CSV using the current file location

try:
    survey_df = pd.read_csv(survey_path)  # tries to load the CSV file into a DataFrame
except FileNotFoundError:
    st.warning("Survey data not found. Please upload or check the CSV path.")  # if the file is missing, display a warning in the Streamlit app
    survey_df = pd.DataFrame()  # fallback: create an empty DataFrame so the app doesn't crash or break later on

# 🧭 Check if the user selected the "Verse Finder" page from the sidebar menu
if page == "Verse Finder":
    # 🖼️ Display a styled HTML title and subtitle for the "Verse Finder" feature of the app
    st.markdown(""" <div class='title'> Emotional Journal & Guidance ✝️</div> <div class='subtitle'>Fuel Your Feelings With Faith 💖✨</div>""", unsafe_allow_html=True)

    # 📋 Add a 3-step instructional guide in a styled box to help users understand how to use the app
    st.markdown("""
        <div class='description-box'>
            <div class='step step-1'>📝 <strong>Step 1:</strong> Type out how you're feeling in the box below. Be honest and open! 💬</div>  
            <div class='step step-2'>🔍 <strong>Step 2:</strong> Click the <em>Reveal Scripture 🌟</em> button to find encouragement.</div>  
            <div class='step step-3'>📖 <strong>Step 3:</strong> Read and reflect on 3 personalized verses + spiritual guidance. 🙏</div>  
            <br>  
            <div style="font-size: 17px; font-weight: bold; color: #6a1b9a;">
            🌈 <strong>Why This App?</strong><br><br>  # Subheading: Why this tool matters
            Sometimes our emotions feel like too much to carry alone. This app helps you name those feelings and match them with verses full of hope, strength, and peace. God’s Word speaks directly into your situation—let it lift you up today! 🌟 
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 💬 Add another section prompting the user to reflect on how they're currently feeling, with an example
    st.markdown("""
        <div style='text-align: center; font-size: 22px; color: #5b2c6f; font-weight: bold; margin-top: 30px;'>
            💬 How are you feeling today?  
        </div>
        <div style='text-align: center; font-size: 15px; color: #7d3c98; margin-top: 8px;'>
            ✏️ Example: "I feel overwhelmed with school and unsure of the future."  
        </div>
    """, unsafe_allow_html=True)

    # 📥 This creates a big text box where users can type in how they feel (free text)
    user_input = st.text_area(" ", height=180, help="Ex: 'I'm overwhelmed with school and feeling uncertain about my future.'")  # user input is stored in user_input variable

    # ⚙️ Define a helper function to process user input and extract emotional keywords using spaCy NLP
    @st.cache_data  # cache the result to avoid re-processing same input multiple times
    def extract_emotions(text):
        doc = nlp(text)  # use the spaCy language model to tokenize and process the input
        return list(set([  # remove duplicates by turning it into a set, then back to a list
            token.lemma_.lower()  # get the base form (lemma) of the word and make it lowercase
            for token in doc  # go through each token in the processed text
            if token.pos_ in ("NOUN", "ADJ", "VERB") and len(token.text) > 2  # only keep nouns, adjectives, and verbs that are longer than 2 characters
        ]))
    # 🔍 Function to find up to 3 Bible verses that match any of the extracted emotion keywords
    def find_top_verses(keywords):
        matches = df[df['Primary Emotion'].apply(lambda x: any(kw in x for kw in keywords))]  # filter the DataFrame to rows where any keyword is in the emotion column
        return matches.sample(min(3, len(matches))) if not matches.empty else pd.DataFrame()  # return up to 3 random matches, or an empty DataFrame if there are none

    # 🎯 When the user clicks the “Reveal Scripture” button, this whole section runs
    if st.button("🔎 Reveal Scripture 🌟"):
        if user_input.strip():  # make sure the input box isn't empty (i.e., user typed something)
            with st.spinner('✨ Reflecting on your words and finding hope in Scripture...'):  # show a little animation while we process
                keywords = extract_emotions(user_input)  # get emotion keywords from user input using spaCy
                st.markdown(f"### 🧠 Emotions Detected: {', '.join(keywords)}")  # display the keywords we found

                results = find_top_verses(keywords)  # search for verses that match those keywords

                if not results.empty:  # if we actually found any matching verses
                    st.markdown("## 📖 Your Verses:")  # display section heading
                    for _, row in results.iterrows():  # loop through each matching verse row
                        st.markdown(f"""
                        <div class='verse-box'>
                            <strong>{row['Bible Verse']}</strong><br> 
                            <em>{row['Primary Emotion'].capitalize()}</em><br><br>  
                            {row['Verse Text']}  # show the actual verse text
                            <div class='explanation-box'>💡 <strong>Reflection:</strong> {row['Explanation']}</div> 
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.warning("🙏 No matching scriptures found. Try different wording or another feeling.")  # fallback if nothing matched
        else:
            st.warning("Please describe how you're feeling to receive guidance.")  # if the input was empty, nudge the user to write something

    # 🌞 Just some rotating positive affirmations to encourage the user (randomly selected)
    encouragements = [
        "🌸 You are fearfully and wonderfully made.",
        "🌿 Be still and know that I am God.",
        "🌈 You are never alone in Christ.",
        "🌻 Let faith guide you today.",
        "☀️ God’s light is with you always."
    ]

    # ✨ Display the encouragement and a small disclaimer at the bottom
    st.markdown(f"""
        <br><hr>
        <div style='text-align: center; font-style: italic; color: #7d3c98; animation: fadeIn 2s;'>
            {random.choice(encouragements)}  
        </div>
        <div style='text-align: center;'>
            <p style='font-size: 13px; color: #999;'>This app is a spiritual companion, not a substitute for prayer or pastoral counsel.</p>  
        </div>
    """, unsafe_allow_html=True)

# ========================== EMOTIONAL DISCOVERY QUIZ TAB ==========================

# 🎯 If the user selected the "Emotional Quiz" tab from the sidebar
if page == "Relief Activity Assessment":
    import numpy as np  # just in case we do any calculations later

    # 🗂 Load the self-care activities CSV (must be in the same folder as this file)
    activity_path = os.path.join(os.path.dirname(__file__), "self_care_activities_updated.csv")
    activity_df = pd.read_csv(activity_path)  # file includes: Activity, Emotion, Description

    # 🧠 Animated glowing title
    st.markdown("""
    <hr><br>
    <div style='text-align: center; font-size: 26px; font-weight: bold; color: #6a1b9a;'>
        🌈 Relief Activity Assessment
    </div>
    """, unsafe_allow_html=True)

    # ✨ Description of how this quiz works
    st.markdown("""
    <div class='description-box'>
    ✨ Check all the statements that you relate to right now.
    We'll figure out which emotion is showing up the most — and give you a glowing self-care activity to help with it. 💜
    </div>
    """, unsafe_allow_html=True)

    # 🧪 Define emotion categories and their associated statements
# 🧪 Define emotion categories and their associated statements
# 🧪 Define emotion categories and their associated statements
    emotion_questions = {
    "Joy": [
        "I feel grateful for my life right now.",
        "I’ve been smiling or laughing a lot lately.",
        "I feel connected to people around me."
    ],
    "Overwhelm": [
        "I have way too much on my plate.",
        "My thoughts are racing and hard to manage.",
        "Even small tasks feel exhausting."
    ],
    "Guilt": [
        "I keep thinking about things I wish I’d done differently.",
        "I feel like I’ve let someone down.",
        "I’m being really hard on myself."
    ],
    "Anxiety": [
        "I’m constantly worried about what’s coming next.",
        "I feel nervous even when nothing is wrong.",
        "My body feels tense or on-edge."
    ]
}
    emotion_scores = {}
# ✨ Emoji mapping for each emotion
    emoji_map = {
    "Joy": "🌞",
    "Overwhelm": "🌀",
    "Guilt": "😔",
    "Anxiety": "😰"
}

# 🎨 Emotion color styles
    color_styles = {
    "Joy": "#ffe9f9",         # light pink
    "Overwhelm": "#fffbd8",   # light yellow
    "Guilt": "#e8e6ff",       # soft lavender
    "Anxiety": "#e0f7ff"      # pale blue
}

    border_styles = {
    "Joy": "#e75480",         # bright pink
    "Overwhelm": "#ffb347",   # soft orange
    "Guilt": "#9370db",       # medium purple
    "Anxiety": "#1e90ff"      # blue
}

# 🔄 Display each question in its own fun glowing box
# Initialize emotion scores dictionary
    emotion_scores = {}

# ✅ Emotion questions, each paired with a custom emoji and color scheme
    styled_questions = [
    {"text": "I feel grateful for my life right now.", "emoji": "🌞", "bg": "#fffbe6", "border": "#f9d342", "emotion": "Joy"},
    {"text": "I’ve been smiling or laughing a lot lately.", "emoji": "😄", "bg": "#ffe9f9", "border": "#ff8fab", "emotion": "Joy"},
    {"text": "I feel connected to people around me.", "emoji": "💞", "bg": "#e0f7fa", "border": "#00acc1", "emotion": "Joy"},

    {"text": "I have way too much on my plate.", "emoji": "📋", "bg": "#fff8dc", "border": "#f4a261", "emotion": "Overwhelm"},
    {"text": "My thoughts are racing and hard to manage.", "emoji": "💭", "bg": "#f0f4ff", "border": "#6a5acd", "emotion": "Overwhelm"},
    {"text": "Even small tasks feel exhausting.", "emoji": "🛌", "bg": "#f9ebff", "border": "#b388eb", "emotion": "Overwhelm"},

    {"text": "I keep thinking about things I wish I’d done differently.", "emoji": "🤔", "bg": "#f5f5f5", "border": "#a9a9a9", "emotion": "Guilt"},
    {"text": "I feel like I’ve let someone down.", "emoji": "💔", "bg": "#ffe0e0", "border": "#e57373", "emotion": "Guilt"},
    {"text": "I’m being really hard on myself.", "emoji": "😓", "bg": "#fff3e0", "border": "#ffb74d", "emotion": "Guilt"},

    {"text": "I’m constantly worried about what’s coming next.", "emoji": "😰", "bg": "#e0f2ff", "border": "#40c4ff", "emotion": "Anxiety"},
    {"text": "I feel nervous even when nothing is wrong.", "emoji": "😬", "bg": "#edf7fa", "border": "#29b6f6", "emotion": "Anxiety"},
    {"text": "My body feels tense or on-edge.", "emoji": "💢", "bg": "#f0ffff", "border": "#81d4fa", "emotion": "Anxiety"},
]

# 🧮 Track scores per emotion
    emotion_scores = {}

    st.markdown("### ✍️ Check all that apply to you:")

# 🔁 Render each question with matching emoji and styles
    for i, q in enumerate(styled_questions):
        key = f"q_{i}"
        col1, col2 = st.columns([1, 12])

        with col1:
            is_checked = st.checkbox("", key=key)

        with col2:
            st.markdown(f"""
            <div style='
                background-color: {q['bg']};
                border-left: 6px solid {q['border']};
                border-radius: 15px;
                padding: 15px;
                margin-bottom: 10px;
                box-shadow: 0 0 10px {q['border']}66;
                font-size: 16px;
                display: flex;
                align-items: center;
            '>
                <span style='font-size: 20px; margin-right: 10px;'>{q['emoji']}</span>
                <span>{q['text']}</span>
            </div>
        """, unsafe_allow_html=True)

        if is_checked:
            emotion = q['emotion']
            emotion_scores[emotion] = emotion_scores.get(emotion, 0) + 1

# 🧠 Submission + Self-Care Recommendation
    if st.button("💡 Reveal My Self-Care Activity"):
        if emotion_scores:
            top_emotion = max(emotion_scores, key=emotion_scores.get)
            matches = activity_df[activity_df["Emotion"].str.lower() == top_emotion.lower()]

            if not matches.empty:
                row = matches.sample(1).iloc[0]
            else:
                row = activity_df.sample(1).iloc[0]
                top_emotion = row["Emotion"]

            st.success(f"💫 You may be feeling **{top_emotion}**.")
            st.markdown(f"""
            <div class='verse-box'>
                <strong>🌟 {row['Activity']}</strong><br><br>
                <div class='explanation-box'>
                    {row['Description']}
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("Please check at least one box to get a personalized suggestion.")
