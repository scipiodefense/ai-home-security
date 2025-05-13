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

# Upload section
st.header("🔍 Upload a Home Security Video")
uploaded_file = st.file_uploader("Choose a video", type=["mp4", "avi", "mov"])
if uploaded_file:
    st.success("Video uploaded!")
    st.video(uploaded_file)

# Placeholder for alerts
st.markdown("### ⚠️ Detected Events")
with st.expander("🕒 Latest Events"):
    st.info("No events detected yet. This section will show alerts once AI detection is added.")

# Footer
st.markdown("---")
st.caption("Developed by Dr. Oscar Neyra • Powered by Python + Streamlit")

