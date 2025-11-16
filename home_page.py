import streamlit as st
import base64
from pathlib import Path

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="🐟 Fish Classification Dashboard",
    page_icon="🐟",
    layout="wide"
)

# ---------- HELPER: CONVERT IMAGE TO BASE64 ----------
def get_base64_image(file):
    """
    Accepts a file path (str) or a file-like object (Streamlit upload)
    """
    try:
        if isinstance(file, str) and Path(file).exists():  # file path exists
            with open(file, "rb") as f:
                data = f.read()
        else:  # file-like object
            data = file.read()
        return base64.b64encode(data).decode()
    except Exception as e:
        st.warning(f"Could not load background image: {e}")
        return None

# ---------- BACKGROUND IMAGE ----------
default_img_path = "images/pexels-quang-nguyen-vinh-222549-2131967.jpg"
uploaded_file = st.file_uploader("Upload a background image (optional)", type=["jpg","jpeg","png"])

bg_image = uploaded_file if uploaded_file is not None else default_img_path
img_base64 = get_base64_image(bg_image)

if img_base64:
    st.markdown(f"""
        <style>
        .stApp {{
            background: url("data:image/jpg;base64,{img_base64}") no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
    """, unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown(
    "<div class='main-title'>🐟 Multiclass Fish Image Classification Dashboard</div>",
    unsafe_allow_html=True
)
