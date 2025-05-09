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

# 📌 Showcase technical skills at the top of the app
# 💼 Highlight tech stack used in the project (collapsed by default to keep UI clean)
with st.expander("🛠️ Tools & Skills Behind This App 🛠️", expanded=False):
    st.markdown("""
    ### 💡 Core Technologies
    - 🐍 **Python 3.11** — scripting the full app logic and data flows
    - 📦 **Streamlit** — for building a sleek, interactive frontend without heavy web dev overhead
    - 🧠 **spaCy NLP** — natural language processing to extract emotional keywords from user reflections
    - 📊 **pandas** — efficient dataframe operations for parsing verse & activity data
    - 🎨 **HTML/CSS** — custom design elements including animated containers, styled boxes, and typography
    - 🖼️ **Base64 Image Embedding** — persistent background image integration with smooth scaling and repeat tiling
    - 🗂️ **CSV Integration** — self-authored emotion-linked verse and activity datasets for easy updates and scalability

    ### 🧪 Additional Enhancements
    - 🧠 Emotion detection logic that filters and scores text input dynamically
    - ✨ Page-specific styling to create distinct emotional aesthetics
    - 📁 Custom file paths, exception handling, and default fallback behavior to ensure app stability
    - 📜 Modular logic for scalability — ready for future expansion (user authentication, journaling, etc.)

    ---
    **💬 Development Reflection**

    This project began as a simple emotional Bible verse tool, but evolved into a full-fledged, emotionally intelligent web app through iterative design and feature layering. The NLP logic was refined over multiple rounds of testing, while UI decisions focused on aligning spiritual warmth with tech-driven interactivity. Careful attention was paid to UX aesthetics and accessibility, with dynamic feedback mechanisms, color-coded verse categories, and personalized suggestions to enrich the user journey.  
    This app is not just a project — it’s a demonstration of emotional design, modular code architecture, and user-first thinking.
    """)


import base64  # Built-in Python module to encode the image in Base64 format
# Define a function that takes the path of an image and returns a Base64-encoded string version of it
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:  # Open the image in binary (readable by the computer) mode
        encoded = base64.b64encode(image_file.read()).decode()  # Encode it in Base64 and convert it into a string
    return encoded  # Return the encoded string so it can be used in CSS
# Build the full file path to the image you uploaded in the "data" folder
image_path = os.path.join(os.path.dirname(__file__), "data", "purple.png")
# Call the helper function to get the Base64-encoded version of the image
base64_image = get_base64_image(image_path)
# Create a CSS style block that uses the Base64 image as a background


# THEN define your sidebar navigation menu
page = st.sidebar.radio("Navigate", ["Home", "Verse Finder", "Relief Activity Assessment"])

# Load spaCy NLP model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    st.error("Please install the spaCy model: `python -m spacy download en_core_web_sm`")
    st.stop()

# Load the Bible verse dataset
csv_path = os.path.join(os.path.dirname(__file__), "data", "Final_Emotional_Bible.csv")
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
    <h4 style='color: #5e35b1;'>🧠💖 Welcome to Wellness — Emotional Reflection Meets Biblical Truth</h4>
    <p style='font-size: 16px; color: #4a235a;'>
    This interactive app helps you <strong>process your feelings</strong> and <strong>find hope in Scripture</strong>. Whether you want to <strong>write out your thoughts</strong> or <strong>answer simple reflection questions</strong>, Wellness uses smart <strong>language detection (spaCy NLP)</strong> and <strong>curated Bible verse matching</strong> to connect your emotions with <strong>personalized spiritual encouragement</strong>.
    </p>
    <p style='font-size: 16px; color: #4a235a;'>
    ✍️ <strong>Verse Finder</strong> — Write how you feel, and get matched with verses that speak directly to your heart.<br>
    🧩 <strong>Relief Activity Assessment</strong> — Check statements that sound like you, and discover your top emotion along with a self-care activity to help you move forward.
    </p>
    <p style='font-size: 16px; color: #4a235a;'>
    At its core, Wellness reminds you that <strong>your emotions matter</strong> — and that <strong>God’s Word offers peace, comfort, and direction</strong> for whatever you’re facing today.
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
# 💡 This block injects a persistent background image using CSS
# It targets `.stApp`, which is Streamlit’s actual container element

st.markdown(f"""
<style>
.stApp {{
    background-image: url("data:image/png;base64,{base64_image}");  /* Set the background using your encoded image */
    background-size: cover;               /* Make the image scale to the full page */
    background-repeat: repeat;            /* Repeat pattern (good for polka dots) */
    background-attachment: fixed;         /* Prevent background from scrolling with page */
    background-position: center;          /* Center it for balance */
    z-index: -1;                           /* Push it to the very back */
}}

/* Ensure default body background doesn’t override this */
html, body {{
    background-color: transparent !important;  /* Make base layer see-through */

}}

html, body, [class*="css"] {{
    background-image: url("data:image/png;base64,{base64_image}");
    background-size: cover;
    background-repeat: repeat;
    background-attachment: fixed;
    color: #2e003e;
    font-family: 'Georgia', serif;
    animation: fadeInBody 2s ease-in;
}}

.title {{
    text-align: center;  /* center-aligns the title */
    color: #5b2c6f;  /* heading color */
    font-size: 60px;  /* pretty big title */
    margin-bottom: 10px;  /* spacing under the title */
    animation: floatTitle 2s ease-in-out infinite alternate;  /* makes it float/vibe */
}}

.subtitle {{
    text-align: center;  /* subtitle is centered too */
    font-size: 24px;  /* smaller than title but still noticeable */
    color: #8e44ad;  /* a lighter purple for contrast */
    margin-bottom: 30px;  /* gives room below it */
    animation: fadeIn 3s ease-in;  /* soft intro animation */
}}

.description-box {{
    background: #fff8fc;  /* pale pink background */
    padding: 25px;  /* some internal spacing */
    border-radius: 20px;  /* rounded corners for softness */
    border: 3px dashed #c39bd3;  /* makes it look scrapbook-y */
    font-size: 17px;  /* readable but not too big */
    margin-bottom: 30px;  /* space under the box */
    animation: riseIn 1.5s ease-in-out;  /* the box kind of “lifts in” */
}}

.step {{
    padding: 15px;  /* padding for each step block */
    border-radius: 12px;  /* rounded steps */
    font-size: 16px;  /* consistent with body text */
    margin: 10px 0;  /* space between steps */
    font-weight: bold;  /* so they stand out */
}}

.step-1 {{ background-color: #ffe4ec; border-left: 6px solid #ff5c8a; }}  /* pink step */
.step-2 {{ background-color: #e0f7fa; border-left: 6px solid #26c6da; }}  /* blue step */
.step-3 {{ background-color: #f1f8e9; border-left: 6px solid #9ccc65; }}  /* green step */

.verse-box {{
    background: #fff0f9;  /* light pink box for the Bible verse area */
    border-left: 6px solid #e75480;
    padding: 18px;
    margin: 20px 0px;
    border-radius: 14px;
    animation: glowFade 3s ease-in-out infinite alternate;
}}

.explanation-box {{
    background-color: #e2f0ff;
    border-left: 6px solid #2980b9;
    padding: 12px;
    margin-top: 8px;
    border-radius: 10px;
    font-size: 15px;
    color: #154360;
    animation: slideInLeft 2s ease-out;
}}

@keyframes fadeInBody {{
    from {{opacity: 0;}}
    to {{opacity: 1;}}
}}

@keyframes fadeIn {{
    0% {{opacity: 0; transform: translateY(10px);}}
    100% {{opacity: 1; transform: translateY(0);}}
}}

@keyframes floatTitle {{
    0% {{transform: translateY(0);}}
    100% {{transform: translateY(-10px);}}
}}

@keyframes riseIn {{
    from {{transform: translateY(40px); opacity: 0;}}
    to {{transform: translateY(0); opacity: 1;}}
}}

@keyframes glowFade {{
    from {{box-shadow: 0 0 8px #ffddee;}}
    to {{box-shadow: 0 0 24px #ff99dd;}}
}}

@keyframes slideInLeft {{
    from {{opacity: 0; transform: translateX(-30px);}}
    to {{opacity: 1; transform: translateX(0);}}
}}
</style>
""", unsafe_allow_html=True)

# 📊 Load the emotional survey data CSV — this dataset includes descriptions and biblical interpretations for different emotions
survey_path = os.path.join(os.path.dirname(__file__), "data", "Christian_Emotions_Interpretation_Survey_Extended.csv")

try:
    survey_df = pd.read_csv(survey_path)  # tries to load the CSV file into a DataFrame
except FileNotFoundError:
    st.warning("Survey data not found. Please upload or check the CSV path.")  # if the file is missing, display a warning in the Streamlit app
    survey_df = pd.DataFrame()  # fallback: create an empty DataFrame so the app doesn't crash or break later on

# 🧭 Check if the user selected the "Verse Finder" page from the sidebar menu
if page == "Verse Finder":
    # 🖼️ Display a styled HTML title and subtitle for the "Verse Finder" feature of the app
    st.markdown(""" <div class='title'> Emotional Journal & Guidance </div> <div class='subtitle'>Fuel Your Feelings With Faith 💖✨</div>""", unsafe_allow_html=True)

    # 📋 Add a 3-step instructional guide in a styled box to help users understand how to use the app
    st.markdown("""
        <div class='description-box'>
            <div class='step step-1'>📝 <strong>Step 1:</strong> Type out how you're feeling in the box below. Be honest and open! 💬</div>  
            <div class='step step-2'>🔍 <strong>Step 2:</strong> Click the <em>Reveal Scripture 🌟</em> button to find encouragement.</div>  
            <div class='step step-3'>📖 <strong>Step 3:</strong> Read and reflect on 3 personalized verses + spiritual guidance. 🙏</div>  
            <br>  
            <div style="font-size: 17px; font-weight: bold; color: #6a1b9a;">
            🌈 <strong>Why This App?</strong><br><br>  Why this tool matters
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
    # 🧠 This function uses spaCy to process user input and extract only emotion-related words
    @st.cache_data  # ⚡ Caches the result to avoid re-running NLP on the same input
    def extract_emotions(text):
        doc = nlp(text)  # 🧠 spaCy processes the input string and breaks it into tokens

        # ✅ Step 1: Pull a clean list of all emotion names in your CSV (lowercase + stripped of whitespace)
        emotion_list = (
            df['Primary Emotion']          # grab the column with emotion labels
            .dropna()                      # remove any missing values (just in case)
            .str.lower()                   # make everything lowercase for comparison
            .str.strip()                   # remove any leading/trailing spaces
            .unique()                      # get unique emotion names only
            .tolist()                      # convert from Series to plain Python list
        )
        # 🔍 Step 2: Look through each word the user wrote and only keep it if it’s in the emotion list
        emotion_keywords = list(set([                        # use a set to avoid duplicates, then turn it into a list
            token.lemma_.lower().strip()                     # use the base form (lemma) of the word, lowercase and trimmed
            for token in doc                                 # go through each token in the user's text
            if token.lemma_.lower().strip() in emotion_list  # only keep it if it's an actual emotion
        ]))

        return emotion_keywords  # ✅ Return a list of detected emotion keywords (like: "anxious", "grateful")

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
    activity_path = os.path.join(os.path.dirname(__file__), "data", "self_care_activities_updated.csv")
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

    # 🧮 Initialize an empty dictionary to store how many times each emotion was selected
    emotion_scores = {}

    # 📝 Display a header prompting the user to check the statements that apply to them
    st.markdown("### ✍️ Check all that apply to you:")

    # 🔁 Loop through each question in the styled_questions list to display them one by one
    for i, q in enumerate(styled_questions):
        key = f"q_{i}"  # Create a unique key for each checkbox so Streamlit can track it

        # 🔲 Split the row into two columns: one small (for checkbox), one large (for the question text)
        col1, col2 = st.columns([1, 12])

        with col1:
            # ✅ Render a checkbox in the small column; user can check it if they relate to the statement
            is_checked = st.checkbox("", key=key)

        with col2:
            # 💬 Render the styled question in the larger column with background color, emoji, and border
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

        # 📈 If the checkbox is selected, increment the count for that emotion
        if is_checked:
            emotion = q['emotion']  # Get the emotion category for this question
            # Add 1 to the score for that emotion, or start at 1 if it doesn’t exist yet
            emotion_scores[emotion] = emotion_scores.get(emotion, 0) + 1

    # 🧠 After user finishes the quiz and clicks the button, show their emotion + self-care tip
    if st.button("💡 Reveal My Self-Care Activity"):
        if emotion_scores:
            # 🔍 Find the emotion that was selected the most by the user
            top_emotion = max(emotion_scores, key=emotion_scores.get)

            # 📄 Filter the activity DataFrame to only rows matching the top emotion
            matches = activity_df[activity_df["Emotion"].str.lower() == top_emotion.lower()]

            # 🎯 If any matching activity exists, pick one randomly; if not, choose from the whole list
            if not matches.empty:
                row = matches.sample(1).iloc[0]  # Pick one random row
            else:
                row = activity_df.sample(1).iloc[0]  # Fallback: pick any random row
                top_emotion = row["Emotion"]  # Update top_emotion to reflect the selected random row

            # ✅ Display the emotion back to the user in a success box
            st.success(f"💫 You may be feeling **{top_emotion}**.")

            # 📦 Show the self-care activity in a styled box with a description
            st.markdown(f"""
            <div class='verse-box'>
                <strong>🌟 {row['Activity']}</strong><br><br>  
                <div class='explanation-box'>
                    {row['Description']}  
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            # ⚠️ If no checkboxes were selected, ask user to check at least one
            st.warning("Please check at least one box to get a personalized suggestion.")
