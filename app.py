import streamlit as st
import tempfile
from analyzer import analyze_video

st.set_page_config(page_title="Home Security AI", layout="wide")

password = st.text_input("Enter password:", type="password")
if password != "supersecret":
    st.stop()

st.markdown("<h1 style='text-align: center;'>🏠 AI Home Security Dashboard</h1>", unsafe_allow_html=True)
st.markdown("#### Upload a video to run fall and person detection")

uploaded_file = st.file_uploader("Choose a video", type=["mp4", "avi", "mov"])
if uploaded_file:
    st.video(uploaded_file)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp:
        temp.write(uploaded_file.read())
        result = analyze_video(temp.name)

    st.markdown("### 🧠 Analysis Result")
    st.info(result)

