import streamlit as st
import time
import random

st.set_page_config(page_title="Scipio AI Ops | Real-Time Surveillance", layout="wide")

# === DARK MODE CUSTOMIZATION ===
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

# === SIDEBAR ===
st.sidebar.title("🧭 Scipio Ops Nav")
nav = st.sidebar.radio("Access Panel", ["🛰️ Command View", "🧠 AI Monitor", "📞 Emergency Ops", "📡 Threat Graphs"])

# === COMMAND CENTER ===
if nav == "🛰️ Command View":
    st.markdown("<h1 style='text-align: center; color:#39ff14;'>🛰️ SCIPIO AI COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.caption("Real-Time Home Surveillance • YC 2025 Demo • AI Secured")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### 🎯 Tactical Feed – Living Room")
        st.video("demo_fall.mp4")
        st.caption("CAM-005-LR • Encrypted • Status: ✅ Online")

    with col2:
        st.markdown("### 🔐 AI Event Summary")
        st.metric("⚠️ Fall Detected", "1", "+1")
        st.metric("🧥 Suspicious Behavior", "0")
        st.metric("📞 Emergency Calls", "1", "+1")
        st.metric("👤 People Detected", "12", "+3")

    st.divider()
    st.markdown("### 🧰 Live Event Log")
    st.code("""
[00:00] AI system initialized.
[00:02] Human presence detected.
[00:17] ⚠️ Sudden collapse (confidence 91.3%).
[00:18] 📞 AI Agent initiated emergency dispatch protocol.
[00:21] ✅ Human response confirmed.
""")

# === AI MONITOR ===
elif nav == "🧠 AI Monitor":
    st.markdown("## 🧠 Neural Intelligence Analysis")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### 📈 Fall Confidence Stream")
        data = [random.randint(40, 60) for _ in range(10)] + [86, 91, 93, 88, 85]
        st.line_chart(data)

    with col2:
        st.markdown("### 🧬 Risk Indices")
        st.metric("Fall Risk", "High", "+23%")
        st.metric("Intrusion Risk", "Low", "-8%")

    st.markdown("### 🕒 Timeline Summary")
    st.markdown("""
- 00:02 — Person enters zone  
- 00:10 — Movement classified  
- 00:17 — ⚠️ Fall trigger  
- 00:18 — 📞 Dispatch: Ambulance  
- 00:20 — Operator acknowledged
""")

# === EMERGENCY PANEL ===
elif nav == "📞 Emergency Ops":
    st.markdown("## 📞 Emergency Dispatch Protocol")

    st.markdown("#### Operator: Dr. Oscar Neyra")
    selected_agency = st.selectbox("Select Emergency Type", ["🚓 Police", "🚑 Ambulance", "🚒 Firefighters"])

    if st.button("🚨 Activate Emergency AI Agent"):
        with st.spinner(f"Connecting AI agent to {selected_agency.split()[1]}..."):
            time.sleep(2)
        st.success(f"✅ AI call placed to {selected_agency.split()[1]} dispatch center.")

        st.markdown("### 🧠 AI Agent Simulation:")
        st.markdown(f"""
        **Scipio AI:** Hello, this is Scipio Autonomous Security Agent.  
        A critical event has occurred at Dr. Neyra's residence.  
        Requesting immediate {selected_agency.split()[1]} dispatch to Culver City.  
        Incident type: {'Fall with possible injury' if selected_agency == '🚑 Ambulance' else 'Unknown threat detected'}.
        """)

    st.divider()
    st.markdown("#### Last Calls")
    st.markdown("- 00:18 — Call: 🚑 Ambulance dispatched by AI")
    st.markdown("- 00:21 — Response confirmed by human")

# === THREAT GRAPH ===
elif nav == "📡 Threat Graphs":
    st.markdown("## 📡 AI Surveillance Intelligence")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🔄 Threat Type Breakdown")
        threat_data = {
            "Fall": random.randint(3, 5),
            "Loitering": random.randint(0, 2),
            "Masked Entry": random.randint(0, 1),
            "No Event": random.randint(10, 20)
        }
        st.bar_chart(threat_data)

    with col2:
        st.markdown("### 🔎 Detection Precision by Model")
        st.markdown("Model V7.3 Confidence Scores")
        st.line_chart([random.uniform(0.6, 0.8) for _ in range(10)] + [0.89, 0.91, 0.94])

    st.markdown("### 🧭 Zone Monitoring Heatmap (Simulated Readout)")
    st.markdown("""
- Zone A (Living Room): 🟥 High Activity  
- Zone B (Backyard): 🟨 Moderate  
- Zone C (Garage): 🟩 Clear  
- Zone D (Entrance): 🟩 Clear
    """)

# === FOOTER ===
st.markdown("---")
st.markdown("<center><small>Scipio AI Intelligence Platform • Confidential • Built by Dr. Oscar Neyra</small></center>", unsafe_allow_html=True)
