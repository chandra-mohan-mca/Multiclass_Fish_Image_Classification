import streamlit as st
import base64

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="🐟 Fish Classification Dashboard",
    page_icon="🐟",
    layout="wide"
)

# ---------- HELPER: CONVERT IMAGE TO BASE64 ----------
def get_base64_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Background image path
img_path = r"c:\\Users\\vnave\\Downloads\\pexels-quang-nguyen-vinh-222549-2131967.jpg"
img_base64 = get_base64_image(img_path)

# ---------- CUSTOM CSS ----------
st.markdown(f"""
    <style>
    /* Background Image */
    .stApp {{
        background: url("data:image/jpg;base64,{img_base64}") no-repeat center center fixed;
        background-size: cover;
    }}

    /* Title */
    .main-title {{
        background: linear-gradient(to right, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.3));
        color: white;
        text-align: center;
        padding: 25px;
        border-radius: 20px;
        font-size: 40px;
        font-weight: bold;
        letter-spacing: 1px;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.8);
        margin-bottom: 25px;
    }}

    /* Section Cards (Glass Effect) */
    .section {{
        background: rgba(0, 0, 0, 0.45);
        backdrop-filter: blur(10px);
        padding: 20px;  /* Force text color to white */
        border-radius: 15px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
        margin-bottom: 20px;
        font-size: 18px;
        line-height: 1.6;
    }}

   
    /* Footer */
    .footer {{
        text-align: center;
        color: white;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.7);
        margin-top: 20px;
    }}
    </style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<div class='main-title'>🐟 Multiclass Fish Image Classification Dashboard</div>", unsafe_allow_html=True)