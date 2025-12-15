import streamlit as st
from PIL import Image

# ---- PAGE CONFIG ----
st.set_page_config(page_title="PursePerch", layout="centered")

# ---- CUSTOM STYLING ----
st.markdown("""
<style>
    .stApp {
        background-color: #fff0f5;
        font-family: 'Helvetica Neue', sans-serif;
    }
    h1, h2, h3 {
        color: #d63384;
        text-align: center;
    }
    .text-box, .cta-box {
        background-color: #ffe6f0;
        padding: 2rem;
        border-radius: 15px;
        border: 1px solid #ffb6c1;
        max-width: 800px;
        margin: 2rem auto;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    .cta-box {
        background-color: #fff5f8;
        border: 2px dashed #d63384;
    }
    blockquote {
        font-style: italic;
        color: #555;
        border-left: 4px solid #d63384;
        margin-left: 0;
        padding-left: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ---- SIDEBAR NAVIGATION ----
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "The Problem", "The Solution", "Market & Customer", "Business Model", "Validation"])

# ---- HOME ----
if page == "Home":
    st.markdown("""
    <div class="text-box">
        <h1>👜 PursePerch</h1>
        <h3>The Chic Safety Clip That’s Redefining Fashion Security</h3>
        <p style='text-align: center;'>PursePerch isn't just a product — it's a movement. We’re bringing peace of mind to nightlife, travel, and daily life by solving the #1 frustration with purses: they don’t stay put.</p>
    </div>
    <div class="text-box">
        <h3>🌟 What is PursePerch?</h3>
        <p><strong>PursePerch</strong> is a discreet magnetic clip that anchors your handbag to your outfit. Think: Apple meets Kate Spade. </p>
        <ul>
            <li>Dual magnetic clips hold your strap to your clothing</li>
            <li>No slipping, swinging, or pickpocket risk</li>
            <li>Offered in elevated finishes for every aesthetic</li>
            <li>Premium version with AirTag tracking for added safety</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.image("https://cdn-icons-png.flaticon.com/512/2730/2730321.png", width=320, caption="Initial Prototype")

    st.markdown("""
    <div class="cta-box">
        <h3>✨ Join the Movement</h3>
        <p>PursePerch is launching soon. Join our waitlist to be first in line for drop notifications, launch-day discounts, and surprise collabs.</p>
    </div>
    """, unsafe_allow_html=True)

    email = st.text_input("Enter your email")
    if st.button("Join the Waitlist"):
        if email:
            st.success(f"Thanks for signing up! We'll keep you posted, {email}.")
        else:
            st.warning("Please enter a valid email address.")

# ---- PROBLEM ----
elif page == "The Problem":
    st.markdown("""
    <div class="text-box">
        <h3>🚨 The Problem</h3>
        <p>Women deserve to feel confident — not burdened by slipping straps or purse anxiety.</p>
        <ul>
            <li>Most purses aren’t hands-free enough for nightlife or travel</li>
            <li>Loss & theft of bags = $2.1B+ in annual damages in the U.S. alone</li>
            <li>Clutches and crossbodies sacrifice style or space</li>
        </ul>
        <p><strong>PursePerch</strong> eliminates all of that. It lets you move — while your bag stays put.</p>
    </div>
    """, unsafe_allow_html=True)

# ---- SOLUTION ----
elif page == "The Solution":
    st.markdown("""
    <div class="text-box">
        <h3>💡 Our Elegant Fix</h3>
        <p>With PursePerch, your strap is secured magnetically — no more adjusting, yanking, or worrying. Simply:</p>
        <ol>
            <li>Slide one magnet inside your top</li>
            <li>Snap the second one on the outside</li>
            <li>Insert your strap between. Done.</li>
        </ol>
        <p>✔️ No damage to fabric<br>
           ✔️ Fashion-forward styling<br>
           ✔️ Optional GPS tracking<br>
           ✔️ Works with any outfit or bag</p>
    </div>
    """, unsafe_allow_html=True)

# ---- MARKET ----
elif page == "Market & Customer":
    st.markdown("""
    <div class="text-box">
        <h3>🎯 Who’s Buying It</h3>
        <p><strong>Women aged 18–34</strong> are our sweet spot — socially active, style-conscious, and safety-aware.</p>
        <ul>
            <li>Concert-goers, bar-hoppers, festival queens</li>
            <li>Urban commuters and college students</li>
            <li>Travelers who want sleek security</li>
        </ul>
        <h4>📈 Market Proof</h4>
        <ul>
            <li>$73B handbag industry (2023)</li>
            <li>6.8% annual growth</li>
            <li>Rising demand for safety wearables + anti-theft accessories</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ---- BUSINESS ----
elif page == "Business Model":
    st.markdown("""
    <div class="text-box">
        <h3>💵 Business Model</h3>
        <p>PursePerch has the margins of an accessory and the emotional stickiness of a lifestyle product.</p>
        <h4>Pricing Tiers</h4>
        <ul>
            <li>$15 — Classic clip in 3 colors</li>
            <li>$25 — Clip + AirTag-ready design</li>
            <li>$30+ — Limited edition collabs</li>
        </ul>
        <h4>Revenue Channels</h4>
        <ul>
            <li>Online DTC (Shopify + Amazon)</li>
            <li>In-store: Sephora, boutiques, airports</li>
            <li>Influencer bundles + gift boxes</li>
        </ul>
        <h4>Economics</h4>
        <ul>
            <li>Cost to produce: ~$2.50</li>
            <li>Gross margins: 75–85%</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ---- VALIDATION ----
elif page == "Validation":
    st.markdown("""
    <div class="text-box">
        <h3>🚀 Traction & Buzz</h3>
        <ul>
            <li>Over 100 interviews: 90% would buy</li>
            <li>Early adopters raved at demo events (Notre Dame, Radius Chicago)</li>
            <li>Prototyped with IDEA Center</li>
            <li>Strong TikTok reactions with soft launch previews</li>
        </ul>
        <blockquote>“This is like the PopSocket of purses — genius.”</blockquote>
        <blockquote>“If this was at checkout in Sephora, I’d buy 3.”</blockquote>
    </div>
    """, unsafe_allow_html=True)

# ---- FOOTER ----
st.markdown("""
---
### 💖 Built by Team Snape
University of Notre Dame | Born in Bars, Built for Life | Let’s perch this purse.
""")