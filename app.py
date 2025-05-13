import streamlit as st
from datetime import datetime

st.set_page_config(page_title="AI Home Security", layout="wide")

# Load secret password
password = st.text_input("Enter password:", type="password")
if password != st.secrets["APP_PASSWORD"]:
    st.stop()

# Sidebar layout
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/616/616408.png", width=100)
st.sidebar.title("🏠 AI Home Security")
st.sidebar.markdown("Secure your home with AI surveillance.")

st.title("📹 Surveillance Dashboard")
st.markdown("Upload footage to detect falls or intruders. Alerts will be shown here when AI is enabled.")

import tempfile
from fall_detector import detect_fall

# Upload section
st.header("🔍 Upload a Home Security Video")
uploaded_file = st.file_uploader("Choose a video", type=["mp4", "avi", "mov"])
if uploaded_file:
    st.video(uploaded_file)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(uploaded_file.read())
        result = detect_fall(temp_video.name)

    if result:
        st.error("⚠️ Fall Detected!")
    else:
        st.success("✅ No Fall Detected.")


# Placeholder for alerts
st.markdown("### ⚠️ Detected Events")
with st.expander("🕒 Latest Events"):
    st.info("No events detected yet. This section will show alerts once AI detection is added.")

# Footer
st.markdown("---")
st.caption("Developed by Dr. Oscar Neyra • Powered by Python + Streamlit")

