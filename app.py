
import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import numpy as np

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("model.pkl", "rb"))

# ---------------- CONFIG ----------------
st.set_page_config(page_title="AI Personality Analyzer", layout="centered")

# ---------------- CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}
.title {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    color: #00f2fe;
}
.subtitle {
    text-align: center;
    color: #ccc;
    margin-bottom: 20px;
}
.section {
    padding: 20px;
    border-radius: 15px;
    background: rgba(255,255,255,0.08);
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<div class='title'>🧠 AI Personality Analyzer</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Industry-Level AI Personality Intelligence 🚀</div>", unsafe_allow_html=True)

# ---------------- INPUT ----------------
st.subheader("📊 Enter Your Daily Habits")

social = st.slider("📱 Social Time", 0, 10)
screen = st.slider("💻 Screen Time", 0, 12)
sleep = st.slider("😴 Sleep", 0, 12)
study = st.slider("📚 Study Hours", 0, 10)

# ---------------- SESSION ----------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- SCORING SYSTEM ----------------
def calculate_score(social, screen, sleep, study):
    score = (study*3 + sleep*2 + social - screen*1.5)
    return round(max(score, 0), 2)

# ---------------- RADAR CHART ----------------
def radar_chart(data):
    categories = ['Social', 'Screen', 'Sleep', 'Study']
    values = data + data[:1]

    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(4,4), subplot_kw=dict(polar=True))
    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.3)

    ax.set_thetagrids(np.degrees(angles[:-1]), categories)

    return fig

# ---------------- AI ANALYSIS ----------------
def ai_analysis(personality, score):
    if personality == "Extrovert":
        base = "You thrive in social environments and gain energy from interaction."
    else:
        base = "You are reflective and perform best in focused environments."

    if score > 20:
        level = "🚀 High Performer"
    elif score > 10:
        level = "⚡ Moderate Performer"
    else:
        level = "⚠️ Needs Improvement"

    return base, level

# ---------------- PREDICT ----------------
if st.button("🚀 Analyze Personality"):

    input_data = pd.DataFrame([[social, screen, sleep, study]],
        columns=["social_time", "screen_time", "sleep_hours", "study_hours"]
    )

    result = model.predict(input_data)[0]
    score = calculate_score(social, screen, sleep, study)

    st.session_state.history.append(result)

    st.markdown("<div class='section'>", unsafe_allow_html=True)

    st.success(f"🎯 Personality: {result}")

    # ---------------- SCORE ----------------
    st.subheader("🧠 Performance Score")
    st.progress(min(score/30, 1.0))
    st.write(f"Score: {score}")

    # ---------------- RADAR ----------------
    st.subheader("📊 Lifestyle Radar")
    fig = radar_chart([social, screen, sleep, study])
    st.pyplot(fig)

    # ---------------- AI ANALYSIS ----------------
    st.subheader("🤖 AI Insights")
    base, level = ai_analysis(result, score)
    st.write(base)
    st.write("Level:", level)

    # ---------------- REPORT ----------------
    report = f"""
AI PERSONALITY REPORT

Personality: {result}
Score: {score}

Habits:
Social: {social}
Screen: {screen}
Sleep: {sleep}
Study: {study}

Insight:
{base}
{level}
"""

    st.download_button("📥 Download Report", report)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- CHAT ----------------
st.subheader("💬 Ask AI")

question = st.text_input("Ask about your habits...")

def smart_chat(q):
    if "improve" in q.lower():
        return "Focus on sleep, reduce screen time, and increase study consistency."
    elif "personality" in q.lower():
        return "Your personality is shaped by your daily habits and environment."
    else:
        return "Small daily improvements lead to massive long-term growth."

if question:
    st.write("🧑 You:", question)
    st.write("🤖 AI:", smart_chat(question))

# ---------------- HISTORY ----------------
if st.session_state.history:
    st.subheader("🧾 Prediction History")
    st.write(st.session_state.history)

# ---------------- FOOTER ----------------
st.markdown("<center style='color:gray;'>Built by Priyansh | AI Project 🚀</center>", unsafe_allow_html=True)
