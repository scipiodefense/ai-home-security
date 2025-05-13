import streamlit as st
from fall_detector import detect_fall
from twilio_alert import send_call
import tempfile

st.set_page_config(page_title="AI Security Dashboard")

# 🔐 Password protection
password = st.text_input("Enter password:", type="password")
if password != "your_secret_password":
    st.stop()

st.title("AI Residential Security Platform")
uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

if uploaded_file:
    st.video(uploaded_file)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
        temp_file.write(uploaded_file.read())
        if detect_fall(temp_file.name):
            st.error("Fall Detected!")
            send_call()
        else:
            st.success("No fall detected.")

