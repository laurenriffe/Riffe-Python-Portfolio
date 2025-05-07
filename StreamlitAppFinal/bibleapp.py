import streamlit as st
import pandas as pd
import spacy
import random
import os

# Set page config
st.set_page_config(page_title="Emotional Bible Guide ✝️", layout="wide")

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    st.error("spaCy model 'en_core_web_sm' not found. Please install it using:")
    st.code("python -m spacy download en_core_web_sm", language="bash")
    st.stop()

# Load the CSV
csv_path = os.path.join(os.path.dirname(__file__), "Final_Emotional_Bible.csv")
if not os.path.exists(csv_path):
    st.error(f"CSV file not found at: {csv_path}")
    st.stop()

try:
    df = pd.read_csv(csv_path)
    df['Primary Emotion'] = df['Primary Emotion'].str.lower().str.strip()
except Exception as e:
    st.error(f"Failed to read the CSV file: {e}")
    st.stop()

# Sidebar Navigation
page = st.sidebar.radio("📚 Navigate", ["Verse Finder", "Feelings Survey", "Learn About Emotions", "Daily Devotion Ideas", "Creative Corner", "Mood Tracker"])

# Styling
st.markdown("""
    <style>
        html, body, [class*="css"] {
            background: linear-gradient(to bottom right, #fef6ff, #e6ccff);
            color: #2e003e;
            font-family: 'Georgia', serif;
            animation: fadeInBody 2s ease-in;
        }
        .title {
            text-align: center;
            color: #5b2c6f;
            font-size: 60px;
            margin-bottom: 10px;
            animation: floatTitle 2s ease-in-out infinite alternate;
        }
        .subtitle {
            text-align: center;
            font-size: 24px;
            color: #8e44ad;
            margin-bottom: 30px;
            animation: fadeIn 3s ease-in;
        }
        .description-box {
            background: #fff8fc;
            padding: 25px;
            border-radius: 20px;
            border: 3px dashed #c39bd3;
            font-size: 17px;
            margin-bottom: 30px;
            animation: riseIn 1.5s ease-in-out;
        }
        .step {
            padding: 15px;
            border-radius: 12px;
            font-size: 16px;
            margin: 10px 0;
            font-weight: bold;
        }
        .step-1 { background-color: #ffe4ec; border-left: 6px solid #ff5c8a; }
        .step-2 { background-color: #e0f7fa; border-left: 6px solid #26c6da; }
        .step-3 { background-color: #f1f8e9; border-left: 6px solid #9ccc65; }
        .verse-box {
            background: #fff0f9;
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
        }
    </style>
""", unsafe_allow_html=True)

if page == "Verse Finder":
    st.markdown("""
        <div class='title'>Emotional Bible Guide ✝️</div>
        <div class='subtitle'>Fuel Your Feelings With Faith 💖✨</div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='description-box'>
            <div class='step step-1'>📝 <strong>Step 1:</strong> Type out how you're feeling in the box below. Be honest and open! 💬</div>
            <div class='step step-2'>🔍 <strong>Step 2:</strong> Click the <em>Reveal Scripture 🌟</em> button to find encouragement.</div>
            <div class='step step-3'>📖 <strong>Step 3:</strong> Read and reflect on 3 personalized verses + spiritual guidance. 🙏</div>
            <br>
            <div style="font-size: 17px; font-weight: bold; color: #6a1b9a;">
            🌈 <strong>Why This App?</strong><br><br>
            Sometimes our emotions feel like too much to carry alone. This app helps you name those feelings and match them with verses full of hope, strength, and peace. God’s Word speaks directly into your situation—let it lift you up today! 🌟
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style='text-align: center; font-size: 22px; color: #5b2c6f; font-weight: bold; margin-top: 30px;'>
            💬 How are you feeling today?
        </div>
        <div style='text-align: center; font-size: 15px; color: #7d3c98; margin-top: 8px;'>
            ✏️ Example: "I feel overwhelmed with school and unsure of the future."
        </div>
    """, unsafe_allow_html=True)

    user_input = st.text_area(" ", height=180, help="Ex: 'I'm overwhelmed with school and feeling uncertain about my future.'")

    @st.cache_data
    def extract_emotions(text):
        doc = nlp(text)
        return list(set([token.lemma_.lower() for token in doc if token.pos_ in ("NOUN", "ADJ", "VERB") and len(token.text) > 2]))

    def find_top_verses(keywords):
        matches = df[df['Primary Emotion'].apply(lambda x: any(kw in x for kw in keywords))]
        return matches.sample(min(3, len(matches))) if not matches.empty else pd.DataFrame()

    if st.button("🔎 Reveal Scripture 🌟"):
        if user_input.strip():
            with st.spinner('✨ Reflecting on your words and finding hope in Scripture...'):
                keywords = extract_emotions(user_input)
                st.markdown(f"### 🧠 Emotions Detected: {', '.join(keywords)}")
                results = find_top_verses(keywords)

                if not results.empty:
                    st.markdown("## 📖 Your Verses:")
                    for _, row in results.iterrows():
                        st.markdown(f"""
                        <div class='verse-box'>
                            <strong>{row['Bible Verse']}</strong><br>
                            <em>{row['Primary Emotion'].capitalize()}</em><br><br>
                            {row['Verse Text']}
                            <div class='explanation-box'>💡 <strong>Reflection:</strong> {row['Explanation']}</div>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.warning("🙏 No matching scriptures found. Try different wording or another feeling.")
        else:
            st.warning("Please describe how you're feeling to receive guidance.")

    encouragements = [
        "🌸 You are fearfully and wonderfully made.",
        "🌿 Be still and know that I am God.",
        "🌈 You are never alone in Christ.",
        "🌻 Let faith guide you today.",
        "☀️ God’s light is with you always."
    ]

    st.markdown(f"""
        <br><hr>
        <div style='text-align: center; font-style: italic; color: #7d3c98; animation: fadeIn 2s;'>
            {random.choice(encouragements)}
        </div>
        <div style='text-align: center;'>
            <p style='font-size: 13px; color: #999;'>This app is a spiritual companion, not a substitute for prayer or pastoral counsel.</p>
        </div>
    """, unsafe_allow_html=True)

elif page == "Feelings Survey":
    st.header("📝 Feelings Survey")
    feeling = st.selectbox("How do you feel today?", ["Joyful", "Anxious", "Hopeful", "Lonely", "Thankful", "Overwhelmed"])
    activities = st.multiselect("Activities that help you feel better:", ["Pray", "Meditate", "Call a friend", "Journal", "Read Scripture", "Rest"])
    prayer = st.text_area("Write a short prayer or affirmation:", height=100)
    if st.button("🙏 Submit Reflection"):
        st.success("Thanks for your reflection! Keep growing in faith 🌱")
        st.write("Your Mood:", feeling)
        st.write("Helpful Activities:", activities)
        st.write("Prayer or Affirmation:", prayer)

elif page == "Learn About Emotions":
    st.header("📚 Learn About Emotions")
    st.markdown("""
    Emotions are part of how God made us. Understanding them helps us grow in faith:

    - 😢 **Sadness** — God comforts us in our grief (Psalm 34:18)
    - 😠 **Anger** — Be slow to anger and quick to forgive (James 1:19)
    - 😨 **Fear** — Trust in God's protection (Isaiah 41:10)
    - 😊 **Joy** — Joy is a fruit of the Spirit (Galatians 5:22)
    - 😔 **Guilt** — We are forgiven and renewed (1 John 1:9)
    """)

elif page == "Daily Devotion Ideas":
    st.header("🙏 Daily Devotion Ideas")
    st.markdown("""
    Use these prompts to build your faith routine:

    - 📖 Read a Psalm each morning
    - ✍️ Keep a nightly gratitude journal
    - 🕯️ Light a candle before prayer
    - 🎶 Play worship music as you reflect
    """)

elif page == "Creative Corner":
    st.header("🎨 Creative Corner")
    prompt = random.choice([
        "Draw a picture of what peace looks like.",
        "Write a poem about God’s love.",
        "List 5 blessings you're thankful for today."
    ])
    st.info(f"🖌️ Creative Prompt: {prompt}")
    response = st.text_area("Express yourself:", height=150)
    if response:
        st.success("Beautiful work! Creativity honors the Creator.")

elif page == "Mood Tracker":
    st.header("📈 Mood Tracker")
    mood_level = st.slider("Rate your current mood:", 0, 10, 5)
    check_pray = st.checkbox("I prayed today")
    check_read = st.checkbox("I read Scripture today")
    check_gratitude = st.checkbox("I practiced gratitude today")
    if st.button("📊 Save Entry"):
        st.success("Mood saved. Come back tomorrow to track your growth 🙌")
        st.write("Mood Level:", mood_level)
        st.write("Prayed:", "Yes" if check_pray else "No")
        st.write("Read Scripture:", "Yes" if check_read else "No")
        st.write("Gratitude:", "Yes" if check_gratitude else "No")
