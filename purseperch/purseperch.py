import streamlit as st
from PIL import Image

# ---- PAGE CONFIG ----
st.set_page_config(page_title="PursePerch", layout="wide")

# ---- CUSTOM STYLING ----
st.markdown("""
<style>
    .stApp {
        background-color: #fff0f5;
        font-family: 'Arial', sans-serif;
    }
    h1, h2, h3 {
        color: #d63384;
    }
    .highlight {
        background-color: #ffe6f0;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #ffc0cb;
    }
    .cta-box {
        background-color: #fff5f8;
        border: 2px dashed #d63384;
        padding: 1rem;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.title("👜 PursePerch")
st.subheader("Safe. Stylish. Savvy. It's time to perch your purse.")

# ---- PRODUCT OVERVIEW ----
st.markdown("""
### 🌟 Introducing PursePerch

**PursePerch** is a patent-pending, fashionable magnetic clip designed to keep your purse exactly where it belongs — on your shoulder. No slipping. No theft. No stress.

- Elegant magnetic system that fastens your purse to your clothing
- Lightweight, non-damaging to fabric
- Comes in chic finishes: Matte Black, Pearl White, Rose Gold
- Optional premium model includes **AirTag** tracking functionality

Perfect for women on the move — bars, clubs, airports, and everywhere in between.
""")

# ---- THE PROBLEM ----
st.markdown("""
---
### 🚨 The Problem
Women constantly report:
- Bags sliding off in social settings
- The need to clutch their purse, limiting movement
- High rates of purse loss/theft (over 1,000 per hour in the U.S.)

Current solutions are:
- Clunky (carabiners)
- Insecure (crossbody switching)
- Unfashionable (anti-theft bags)

There is **no elegant way** to secure a handbag — until now.
""")

# ---- THE SOLUTION ----
st.markdown("""
---
### 💡 The Solution
**PursePerch** elegantly snaps your purse strap in place using a dual-magnet system:
1. Place one magnet inside your shirt
2. Align the second on the outside
3. Slide your purse strap between — it stays perfectly perched

✔️ Keeps your purse in place
✔️ Preserves your look
✔️ Gives you peace of mind

Even better — it’s compatible with most outfits and supports a wide range of strap styles.
""")

# ---- IMAGE (placeholder) ----
st.image("https://cdn-icons-png.flaticon.com/512/2730/2730321.png", caption="Initial PursePerch Prototype", width=300)

# ---- MARKET & CUSTOMER ----
st.markdown("""
---
### 👥 Who We’re For
Our target audience includes:
- **Gen Z & Millennial women** who carry handbags to clubs, bars, events
- **Female travelers** seeking lightweight anti-theft solutions
- **Moms, professionals, and students** who want security without compromising style

### 📈 Market Size
- 👜 $73B handbag industry (2023)
- 🚀 6.8% CAGR through 2032
- 🧳 $7.7B projected anti-theft luggage market by 2032

**PursePerch** sits at the intersection of fashion, security, and convenience.
""")

# ---- PRICING & BUSINESS MODEL ----
st.markdown("""
---
### 💵 Business Model
**Revenue Streams:**
- **Direct-to-Consumer:** via our website, Amazon, and social media
- **Retail Partners:** Sephora, Zara, Ulta Beauty, airport kiosks
- **Wholesale Bundles:** for event venues, gift boxes, and subscription boxes

**Product Tiers:**
- $15 — Base Model: Magnetic clip with color/style options
- $25 — Premium: Magnetic clip + AirTag slot
- $30+ — Seasonal/Designer collaborations

**Estimated Margin:** 70–85%
- Manufacturing cost per unit: ~$2.50
- Packaging: $0.75
- Retail price: $15–$30

### 📦 Go-to-Market
1. Launch with college influencer campaign (Notre Dame, UCLA, NYU)
2. Targeted Instagram/TikTok ads with UGC
3. Soft launch in college bookstores + online preorder portal
""")

# ---- VALIDATION ----
st.markdown("""
---
### ✅ Traction & Validation
- 100+ customer interviews: 90%+ would purchase, 85% willing to pay $15–$30
- MVP prototypes tested on campus with strong positive reactions
- IDEA Center support + prototyping in progress
- $14K projected to launch (materials, packaging, site, basic inventory)

**Feedback Themes:**
- "Finally, something cute AND secure."
- "I’d use this every time I go out."
- "Love the AirTag idea."
""")

# ---- CALL TO ACTION ----
st.markdown("""
---
<div class="cta-box">
    <h3>🚀 Join Our Waitlist</h3>
    Want to be first in line for the launch? Sign up below to receive product updates, discounts, and early access.
</div>
""", unsafe_allow_html=True)

email = st.text_input("Enter your email")
if st.button("Join the Waitlist"):
    if email:
        st.success(f"Thanks for signing up! We'll keep you posted, {email}.")
    else:
        st.warning("Please enter a valid email address.")

# ---- FOOTER ----
st.markdown("""
---
### 💖 Built by Team Snape
University of Notre Dame | MGTO 30500 | Designed with love & hustle 💼✨
""")
