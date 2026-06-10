import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="🧠 ProcrastiScan AI",
    page_icon="🧠",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.block-container {
    max-width: 1100px;
}

.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
}

div[data-testid="stMetric"] {
    background-color: rgba(255,255,255,0.05);
    padding: 15px;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.08);
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO BANNER ----------------

st.markdown("""
<div style='
text-align:center;
padding:25px;
background:linear-gradient(90deg,#6a11cb,#2575fc);
border-radius:15px;
margin-bottom:25px;'>

<h1 style='color:white;'>
🧠 ProcrastiScan AI
</h1>

<p style='color:white;font-size:18px;'>
Discover your productivity patterns and unlock smarter work habits 🚀
</p>

</div>
""", unsafe_allow_html=True)

# ---------------- AI LOGO ----------------

st.image(
    "https://cdn-icons-png.flaticon.com/512/4712/4712109.png",
    width=90
)

# ---------------- GROQ SETUP ----------------

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("🧠 ProcrastiScan AI")

    st.write(
        "Find out why you're procrastinating and get a personalized action plan."
    )

    st.success("⚡ Powered by Groq AI")

    st.caption("Version 1.0")

    st.markdown("---")

    st.write("🧠 Behavioral Insights")
    st.write("📊 Productivity Insights")
    st.write("💡 Motivational Coaching")

# ---------------- MAIN CONTENT ----------------

st.markdown("### 🚀 AI-Powered Productivity Analyzer")

st.info(
    "Enter a task and receive personalized productivity insights and action plans."
)

task = st.text_input("📌 What task are you avoiding?")
deadline = st.text_input("⏳ Deadline")

difficulty = st.selectbox(
    "⚡ Difficulty",
    ["Easy", "Medium", "Hard"]
)

# ---------------- DIFFICULTY INDICATOR ----------------

if difficulty == "Easy":
    st.success("😎 Easy Mission")

elif difficulty == "Medium":
    st.warning("🤔 Challenge Accepted")

else:
    st.error("💀 Boss Level Task")

# ---------------- ANALYSIS BUTTON ----------------

if st.button("🚀 Analyze My Productivity"):

    with st.spinner("Analyzing your productivity patterns..."):

        st.toast("🧠 AI is analyzing your productivity...")

        prompt = f"""
You are ProcrastiScan AI.

Task: {task}
Deadline: {deadline}
Difficulty: {difficulty}

Provide:

1. Procrastination Personality Type
2. Risk Score (out of 100)
3. Urgency Level
4. A short humorous observation
5. Three practical action steps
6. A motivational quote

Keep it concise, helpful and fun.
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

    # ---------------- DASHBOARD METRICS ----------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="🤖 AI Confidence",
            value="95%"
        )

    with col2:
        st.metric(
            label="🧠 Analysis",
            value="Ready"
        )

    with col3:
        st.metric(
            label="⚡ Status",
            value="Active"
        )

    st.markdown("---")

    # ---------------- PRODUCTIVITY ASSESSMENT ----------------

    st.subheader("📊 Productivity Assessment")

    score = 85

    st.progress(score / 100)

    if score > 70:
        st.error("🔴 High Improvement Opportunity")

    elif score > 40:
        st.warning("🟡 Moderate Improvement Opportunity")

    else:
        st.success("🟢 Strong Productivity Habits")

    st.markdown("---")

    # ---------------- AI INSIGHTS ----------------

    st.subheader("🧠 AI Insights")

    st.write(response.choices[0].message.content)

    st.markdown("---")

    st.success(
        "💡 Remember: Starting badly is better than not starting at all."
    )

# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown(
    """
    <div style="
        text-align:center;
        font-size:11px;
        color:gray;
        margin-top:20px;">
        Built by Bharath & Varshini
    </div>
    """,
    unsafe_allow_html=True
)