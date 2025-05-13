import streamlit as st
from datetime import datetime
import tempfile
from analyzer import analyze_video  # 👈 External function

# Set up the layout
st.set_page_config(page_title="Home Security AI", layout="wide")

# Password protection
password = st.text_input("Enter password:", type="password")
if password != "supersecret":
    st.stop()

# Header
st.markdown("<h1 style='text-align: center;'>🏠 AI Home Security Dashboard</h1>", unsafe_allow_html=True)
st.markdown("#### Welcome to your smart surveillance dashboard.")

# Upload section
st.markdown("### 🔍 Upload a Home Security Video")
uploaded_file = st.file_uploader("Choose a video", type=["mp4", "avi", "mov"])

if uploaded_file:
    st.success("Video uploaded!")
    st.video(uploaded_file)

    # Save video to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
        tmp.write(uploaded_file.read())
        result = analyze_video(tmp.name)  # 🔍 Call the external function

    # Show the result
    st.markdown("### 🧠 Analysis Result")
    st.info(result)

