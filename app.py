import streamlit as st
import time
import random

st.set_page_config(page_title="Scipio AI | Command Control", layout="wide")

# === STYLING ===
st.markdown("""
<style>
body, html, [class*='css'] {
    background-color: #0a0c10;
    color: #e6e6e6;
    font-family: 'Consolas', monospace;
}
.stButton>button {
    background-color: #ff004c;
    color: white;
    border-radius: 5px;
    padding: 0.5em 1.5em;
    font-weight: bold;
}
.stMetric {
    color: #00ff9d;
    font-weight: bold;
}
hr {
    border: none;
    height: 1px;
    background: linear-gradient(to right, #00ff9d, transparent);
    margin: 2rem 0;
}
</style>
""", unsafe_allow_html=True)

# === AUTH ===
password = st.text_input("🔐 Secure Access Code:", type="password")
if password != "supersecret":
    st.stop()

# === SIDEBAR ===
st.sidebar.title("🧭 Scipio Ops Navigation")
nav = st.sidebar.radio("Go to:", [
    "🛰️ Mission Panel",
    "🎥 Multicam Grid",
    "📞 AI Emergency Dispatcher",
    "🧠 Threat Intelligence",
    "📂 Incident Timeline"
])

# === MISSION PANEL ===
if nav == "🛰️ Mission Panel":
    st.markdown("<h1 style='text-align: center; color:#00ff9d;'>🛰️ SCIPIO COMMAND OPS</h1>", unsafe_allow_html=True)
    st.caption("Autonomous Threat Analysis • Real-time AI Control Node")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### 🟢 Primary Camera Feed – Zone A")
        st.video("demo_fall.mp4")
        st.caption("CAM-005-LR | Status: Online | Secure Feed")

    with col2:
        st.markdown("### 🧠 AI Alerts Summary")
        st.metric("👵 Fall Detected", "1", "+1")
        st.metric("🚨 Emergency Triggered", "1", "+1")
        st.metric("📡 Model Confidence", "91.3%")
        st.metric("📞 Contact Reached", "Oscar Neyra")

    st.divider()
    st.markdown("### 🗣️ AI Voice Transcript Log")
    with st.expander("View AI-Human Dispatch Communication"):
        st.markdown("""
        **[00:17]** AI: Fall pattern detected in Zone A.
        
        **[00:18]** AI: Dialing emergency contact: +1 (555) 123-4567…
        
        **[00:19]** OSCAR: Hello?
        
        **[00:19]** AI: This is Scipio Autonomous Agent. Grandma has fallen.
        
        **[00:20]** AI: Dispatching Ambulance. ETA 4 mins.
        
        **[00:21]** AI: Returning to monitoring mode.
        """)

# === MULTICAM GRID ===
elif nav == "🎥 Multicam Grid":
    st.markdown("<h2 style='color:#00ff9d;'>🎥 Multicamera Surveillance Grid</h2>", unsafe_allow_html=True)
    cam1, cam2 = st.columns(2)
    cam3, cam4 = st.columns(2)

    with cam1:
        st.video("demo_fall.mp4")
        st.caption("CAM-001 | Zone A – Living Room")
    with cam2:
        st.video("demo_fall.mp4")
        st.caption("CAM-002 | Zone B – Entrance")
    with cam3:
        st.video("demo_fall.mp4")
        st.caption("CAM-003 | Zone C – Backyard")
    with cam4:
        st.video("demo_fall.mp4")
        st.caption("CAM-004 | Zone D – Garage")

# === EMERGENCY DISPATCH ===
elif nav == "📞 AI Emergency Dispatcher":
    st.markdown("## 📞 Emergency Dispatch Interface")
    choice = st.selectbox("Select Emergency Type", ["🚑 Ambulance", "🚓 Police", "🚒 Firefighters"])

    if st.button("🤖 Initiate AI Emergency Call"):
        with st.spinner("Connecting to dispatch network..."):
            time.sleep(2)
        st.success(f"Call to {choice.split()[1]} successfully simulated.")
        st.markdown(f"""
        **AI Agent:**
        Critical incident detected.
        Type: {choice}
        Location: Culver City
        Victim: Elderly female
        Action: Dispatch requested
        """)

# === THREAT INTELLIGENCE ===
elif nav == "🧠 Threat Intelligence":
    st.markdown("## 📊 Threat Intelligence & Graphs")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔄 Threat Breakdown")
        threat_data = {
            "Fall Events": random.randint(1, 3),
            "Loitering": random.randint(0, 2),
            "Masked Entry": random.randint(0, 1),
            "No Event": random.randint(10, 15)
        }
        st.bar_chart(threat_data)

    with col2:
        st.markdown("### ⚙️ Model Confidence")
        st.line_chart([random.uniform(0.72, 0.91) for _ in range(12)])

# === INCIDENT TIMELINE ===
elif nav == "📂 Incident Timeline":
    st.markdown("## 📂 AI-Logged Event Timeline")
    st.markdown("### Case ID: GMA-001 — Fall Detected")
    st.code("""
    [00:17] Fall detected — CAM-005
    [00:18] Dialing: Oscar Neyra
    [00:19] Confirmed: Grandma fell
    [00:20] Dispatch: 🚑 Ambulance
    [00:21] Monitoring resumed
    """)
    st.button("📥 Download Incident Report")

# === FOOTER ===
st.markdown("<hr><center><small>Scipio AI Platform • Command Ops Mode • Built by Dr. Oscar Neyra • YC 2025</small></center>", unsafe_allow_html=True)
