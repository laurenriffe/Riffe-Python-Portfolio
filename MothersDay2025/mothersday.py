import streamlit as st
import pandas as pd
import base64
import os

# ---- Page Configuration ----
st.set_page_config(page_title="Our Family Video Archive", layout="wide")

# ---- Background Styling ----
def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Resolve path to 'photo/background.jpg'
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "photo", "background.jpg")
set_background(image_path)

# ---- Header Section ----
st.markdown("""
    <div style='text-align: center; padding: 2rem; background: linear-gradient(to right, #cde7f9, #92b4ec); border-radius: 25px;'>
        <h1 style='color: #003366; font-size: 3em;'>Welcome to Our Family Video Archive</h1>
        <h3 style='color: #003366;'>Where we celebrate our memories with you, Mom.</h3>
        <p style='font-size: 1.2em; color: #002244; max-width: 700px; margin: auto;'>
            Every laugh, every adventure, every special moment—we’ve captured them here for you to revisit anytime. 
            Thank you for filling our lives with unconditional love, endless encouragement, and unforgettable memories. 
            You are the heart of this family. We love you more than words can say. Happy Mother’s Day.
        </p>
    </div>
""", unsafe_allow_html=True)

# ---- Video Data ----
data = {
    "Title": [
        "Mother's Day 2021: What We Love About You",
        "Mother's Day 2022: Riptide Parody Music Video",
        "Europe Trip 2024: Belgium, Luxembourg & Netherlands",
        "Olympic National Park Trip 2024",
        "2021 Year Recap"
    ],
    "YouTube Link": [
        "https://youtu.be/TA0l3aF0EBM",
        "https://youtu.be/uyaPxac9fwI",
        "https://youtu.be/_EfCTXSeWCg",
        "https://youtu.be/OC5AJ5q6XBA",
        "https://youtu.be/K9yyXh2VjSY"
    ],
    "Year": ["2021", "2022", "2024", "2024", "2021"],
    "Occasion": ["Mother's Day", "Mother's Day", "Trip", "Trip", "Year Recap"],
    "Description": [
        "David and Lauren share what they love most about you, with a special guest appearance from the cats.",
        "We turned 'Riptide' into a personalized music video just for you—dancing, singing, and celebrating our love for you.",
        "Relive our unforgettable European adventure through Belgium, Luxembourg, and the Netherlands.",
        "Experience the beauty of Olympic National Park and our family moments in the great outdoors.",
        "A heartwarming recap of all our family highlights from 2021. Memories to cherish forever."
    ]
}
df = pd.DataFrame(data)

# ---- Filters ----
st.sidebar.header("Filter Your Memories")
year_filter = st.sidebar.selectbox("Select Year", options=["All"] + sorted(df["Year"].unique().tolist()))
occasion_filter = st.sidebar.selectbox("Select Occasion", options=["All"] + sorted(df["Occasion"].unique().tolist()))

filtered_df = df.copy()
if year_filter != "All":
    filtered_df = filtered_df[filtered_df["Year"] == year_filter]
if occasion_filter != "All":
    filtered_df = filtered_df[filtered_df["Occasion"] == occasion_filter]

# ---- Display Videos ----
st.markdown("<hr style='border: 1px solid #dcdcdc;'>", unsafe_allow_html=True)
st.header("Your Curated Video Collection")

if filtered_df.empty:
    st.write("No videos match your selection. Please try different filters.")
else:
    for idx, row in filtered_df.iterrows():
        st.markdown(f"""
            <div style='background: #e6f2ff; border: 2px solid #92b4ec; border-radius: 15px; padding: 1.5rem; margin-bottom: 2rem; box-shadow: 2px 2px 12px #92b4ec;'>
                <h2 style='color: #003366;'>{row['Title']}</h2>
                <p style='color: #002244; font-size: 1.1em;'>{row['Description']}</p>
            </div>
        """, unsafe_allow_html=True)
        st.video(row['YouTube Link'])
        st.markdown("---")
