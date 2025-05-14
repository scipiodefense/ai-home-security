import streamlit as st
import time
import random

# === CONFIG ===
st.set_page_config(page_title="Lisus AI Security", layout="wide")

# === AUTH ===
st.markdown("<h1 style='text-align: center;'>🔐 Secure Login</h1>", unsafe_allow_html=True)
password = st.text_input("Enter your secure access code:", type="password")
if password != "supersecret":
    st.stop()

st.markdown("<h1 style='text-align: center;'>🏠 AI Surveillance Platform</h1>", unsafe_allow_html=True)
st.caption("Lisus AI • Private Beta • YC 2025 Demo")
st.divider()

# === LAYOUT ===
nav = st.sidebar.radio("🔭 View Options", ["Dashboard", "Live Feed", "AI Monitor", "Emergency Panel", "Diagnostics"])

# === DASHBOARD ===
if nav == "Dashboard":
    st.subheader("📊 Real-Time Intelligence Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Active Cameras", "4", "+1")
    col2.metric("Detections Today", "12", "+3")
    col3.metric("Emergency Calls", "1", "0")

    st.markdown("### 📍 Location Map (Simulated)")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/World_map_blank_without_borders.svg/2560px-World_map_blank_without_borders.svg.png", use_column_width=True)

    st.markdown("### 🧠 AI Summary")
    st.markdown("""
    - 🚶‍♂️ 8 Person Events  
    - ⚠️ 2 Fall Alerts  
    - 🧥 1 Masked Intruder Detected  
    """)

# === LIVE FEED ===
elif nav == "Live Feed":
    st.subheader("🎥 Live Feed – Living Room")
    st.video("demo_fall.mp4")
    st.caption("Feed: CAM-005-LR • Status: ✅ Online • AI Status: Monitoring...")

# === AI MONITOR ===
elif nav == "AI Monitor":
    st.subheader("🧠 AI Detection Console")

    st.markdown("#### Fall Detection Timeline")
    st.markdown("- 00:17 — ⚠️ Sudden posture collapse")
    st.markdown("- 00:18 — 📞 Emergency triggered")
    st.markdown("- 00:20 — ✅ Confirmed response")
    st.divider()

    st.markdown("#### Confidence Chart")
    st.line_chart([random.randint(50, 70) for _ in range(10)] + [87, 91, 94, 88])

    st.markdown("#### Current Risk Classification")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Fall Risk", "High", delta="+23%")
    with col2:
        st.metric("Intruder Risk", "Low", delta="-8%")

    st.markdown("#### Pose Snapshot")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/BlankMap-World6.svg/2000px-BlankMap-World6.svg.png", use_column_width=True)


# === EMERGENCY PANEL ===
elif nav == "Emergency Panel":
    st.subheader("📞 Emergency Contact Automation")

    st.markdown("#### Active Contact")
    st.code("📱 +1 (555) 123-4567 – Oscar Neyra")

    if st.button("🚨 Initiate Emergency Call"):
        with st.spinner("Dialing contact..."):
            time.sleep(1.5)
        st.success("Call placed successfully at 00:18 • Acknowledged ✅")

    st.markdown("#### Call Log")
    st.markdown("- 00:18 — Call placed via AI trigger")
    st.markdown("- 00:19 — Acknowledged by Oscar Neyra")
    st.markdown("- 00:21 — Emergency services notified")

# === DIAGNOSTICS ===
elif nav == "Diagnostics":
    st.subheader("🧰 System Health Monitor")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Device Status")
        st.metric("CAM-005-LR", "Online")
        st.metric("CAM-006-BR", "Online")
        st.metric("CAM-007-DR", "Online")
    with col2:
        st.markdown("#### AI Module")
        st.metric("Fall Module", "✅ Active")
        st.metric("Intruder Module", "✅ Active")
        st.metric("Face Matching", "🟠 In Testing")

    st.markdown("#### Internal Logs")
    st.code("""
[INFO] [00:00] System Initialized
[INFO] [00:02] AI Detector Active
[DETECT] [00:17] Fall Event Detected
[ALERT] [00:18] Emergency Contact Triggered
[INFO] [00:21] Response Confirmed
""")

# === FOOTER ===
st.markdown("---")
st.caption("Lisus AI Security | Built by Dr. Oscar Neyra • Streamlit Demo • YC 2025")
