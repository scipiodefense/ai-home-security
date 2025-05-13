import streamlit as st
from datetime import datetime
import tempfile

# Set page layout
st.set_page_config(page_title="AI Home Security", layout="wide")

# Password protection
password = st.text_input("Enter password:", type="password")
if password != st.secrets.get("APP_PASSWORD", "supersecret"):
    st.stop()

# Sidebar
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/616/616408.png", width=100)
st.sidebar.title("🏠 AI Home Security")
st.sidebar.markdown("Secure your home with AI surveillance.")

# Main header
st.title("📹 Surveillance Dashboard")
st.markdown("Upload security footage to simulate AI-based home monitoring.")

# Upload section
st.header("🔍 Upload a Home Security Video")
uploaded_file = st.file_uploader("Choose a video", type=["mp4", "avi", "mov"])

if uploaded_file:
    st.success("Video uploaded successfully!")
    st.video(uploaded_file)

# Placeholder for future alerts
st.markdown("### ⚠️ Detected Events (Demo Only)")
with st.expander("🕒 Latest Alerts"):
    st.info("No AI detection running. This area will show alerts when enabled.")

# Footer
st.markdown("---")
st.caption("Developed by Dr. Oscar Neyra • Powered by Python + Streamlit")

