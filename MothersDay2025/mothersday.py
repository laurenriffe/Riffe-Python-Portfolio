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
        <h3 style='color: #003366;'>Where we celebrate our memories and our love for you!</h3>
        <p style='font-size: 1.2em; color: #002244; max-width: 700px; margin: auto;'>
            So many laughs, adventures, and special moments - we’ve captured them here. 
            Thank you for filling our lives with unconditional love, endless encouragement, and unforgettable memories. 
            You are the heart of this family. We love you more than words can say. Happy Mother’s Day!
        </p>
    </div>
""", unsafe_allow_html=True)

# ---- Video Data ----
data = {
    "Title": [
        "Mother's Day 2025: David",
        "Mother's Day 2021: What We Love About You",
        "Mother's Day 2020: Riptide Parody Music Video",
        "Europe Trip 2024: Belgium, Luxembourg & Netherlands",
        "Olympic National Park Trip 2024",
        "2021 Year Recap"
    ],
    "YouTube Link": [
        "https://youtu.be/9ZpZzDo6TgY",
        "https://youtu.be/TA0l3aF0EBM",
        "https://youtu.be/uyaPxac9fwI",
        "https://youtu.be/_EfCTXSeWCg",
        "https://youtu.be/OC5AJ5q6XBA",
        "https://youtu.be/K9yyXh2VjSY"
    ],
    "Year": ["2025", "2021", "2020", "2024", "2024", "2021"],
    "Occasion": ["Mother's Day", "Mother's Day", "Mother's Day", "Trip", "Trip", "Year Recap"],
    "Description": [
        "David's top 10 things he loves about you and his gratitude for all you do.",
        "We share what we love most about you, with a special guest appearance from the cats.",
        "We turned 'Riptide' into a personalized music video just for you - dancing, singing, and celebrating our love!",
        "Relive our unforgettable European adventure through Belgium, Luxembourg, and the Netherlands.",
        "The beauty of the Olympic National Park and our family moments in the great outdoors.",
        "A recap of all our family highlights from 2021 - So many fun memories!"
    ]
}
df = pd.DataFrame(data)

# ---- Filters ----
st.sidebar.header("Filter Your Memories")
year_filter = st.sidebar.selectbox("Select Year", options=["All"] + sorted(df["Year"].unique(), reverse=True))
occasion_filter = st.sidebar.selectbox("Select Occasion", options=["All"] + sorted(df["Occasion"].unique()))

filtered_df = df.copy()
if year_filter != "All":
    filtered_df = filtered_df[filtered_df["Year"] == year_filter]
if occasion_filter != "All":
    filtered_df = filtered_df[filtered_df["Occasion"] == occasion_filter]

# Sort by Year descending before showing
filtered_df["Year"] = pd.to_numeric(filtered_df["Year"], errors="coerce")
filtered_df = filtered_df.sort_values(by="Year", ascending=False)

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
