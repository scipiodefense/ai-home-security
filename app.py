import streamlit as st
import time
import random

# === GLOBAL SETUP ===
st.set_page_config(page_title="Lisus AI Command | Surveillance Ops", layout="wide")

# === CUSTOM DARK THEME STYLING ===
st.markdown("""
    <style>
        html, body, [class*="css"] {
            background-color: #0f1117;
            color: #e0e0e0;
            font-family: 'Segoe UI', sans-serif;
        }
        .stButton>button {
            background-color: #ff4b4b;
            color: white;
            border-radius: 8px;
            border: none;
        }
        .stMetric {
            color: #39ff14 !important;
        }
    </style>
""", unsafe_allow_html=True)

# === AUTH ===
password = st.text_input("🛡️ Enter Operator Code:", type="password")
if password != "supersecret":
    st.stop()

# === SIDEBAR NAVIGATION ===
st.sidebar.title("🧭 Lisus Ops Nav")
nav = st.sidebar.radio("Access Panel", ["🛰️ Command View", "🎥 Live Feed", "🧠 AI Monitor", "📞 Emergency Ops"])

# === DASHBOARD (Command View) ===
if nav == "🛰️ Command View":
    st.markdown("<h1 style='text-align: center; color:#39ff14;'>🛰️ LISUS AI COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.caption("Mission Dashboard • AI Surveillance Ops • Powered by Lisus")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### 🎯 Tactical Surveillance Feed")
        st.video("demo_fall.mp4")
        st.caption("CAM-005-LR • Encrypted • Status: ✅ Online")

    with col2:
        st.markdown("### 🔐 AI Threat Intelligence")
        st.metric("⚠️ Fall Detection", "1", "+1 event")
        st.metric("🧥 Intruder Detected", "0")
        st.metric("📍 Active Zones", "4/4")
        st.metric("📞 Emergency Events", "1", "+1")

    st.divider()

    col3, col4 = st.columns(2)
    with col3:
        st.markdown("### 📈 Confidence Analysis – AI Fall Monitor")
        confidence_data = [random.uniform(45, 65) for _ in range(10)] + [86, 89, 91, 88, 85]
        st.line_chart(confidence_data)

    with col4:
        st.markdown("### 🕒 Event Timeline")
        st.markdown("""
        - 00:02 — 👤 Entry detected  
        - 00:10 — 🟡 Movement classified  
        - 00:17 — ⚠️ Fall Triggered  
        - 00:18 — 📞 Emergency Protocol Initiated  
        - 00:21 — ✅ Confirmed response
        """)

    st.divider()
    st.markdown("### 🧰 System Log Stream")
    st.code("""
[00:00] [SYS] Initializing CAM-005-LR
[00:02] [AI] Person detected
[00:17] [ALERT] Fall confirmed at 91.3% confidence
[00:18] [CALL] Emergency contact auto-dialed
[00:21] [SYS] Response acknowledgment confirmed
    """)

# === LIVE FEED ===
elif nav == "🎥 Live Feed":
    st.markdown("## 🎥 Mission Visual – CAM-005-LR")
    st.video("demo_fall.mp4")
    st.markdown("Feed Status: 🔒 Encrypted | Frame Rate: 30 FPS | Latency: 12ms")

# === AI MONITOR ===
elif nav == "🧠 AI Monitor":
    st.markdown("## 🧠 Neural Intelligence Analysis")
    st.markdown("### Fall Detection Event Detail")
    st.markdown("- 00:17 — ⚠️ Postural Collapse Detected")
    st.markdown("- 00:18 — 📞 Emergency Protocol Triggered")
    st.markdown("- 00:20 — ✅ Human Acknowledgment Logged")

    st.divider()
    st.markdown("### 🔍 Risk Profiles")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Fall Risk Index", "High", "+23%")
    with col2:
        st.metric("Intruder Risk Index", "Low", "-8%")

    st.markdown("### 🧬 Pose Signature Snapshot")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Human_skeleton_back_en.svg/1280px-Human_skeleton_back_en.svg.png", use_column_width=True)

# === EMERGENCY PANEL ===
elif nav == "📞 Emergency Ops":
    st.markdown("## 📞 Emergency Protocol Interface")
    st.markdown("**Assigned Operator:** Dr. Oscar Neyra\n**Contact Route:** +1 (555) 123-4567")

    if st.button("🚨 Activate Call Protocol"):
        with st.spinner("Initiating encrypted dial..."):
            time.sleep(1.5)
        st.success("✅ Call placed successfully. Response unit acknowledged at 00:19.")

    st.markdown("### Call Engagement Log")
    st.markdown("""
- 00:18 — Call auto-initiated  
- 00:19 — Operator response logged  
- 00:21 — Emergency cleared
    """)

# === FOOTER ===
st.markdown("---")
st.markdown("<center><small>Scipio AI Intelligence Platform • Confidential • © 2025 Dr. Oscar Neyra</small></center>", unsafe_allow_html=True)
