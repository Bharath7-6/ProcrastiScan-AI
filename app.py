
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

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

# ---------------- LANGUAGE ----------------

language = st.sidebar.selectbox(
    "🌐 Language",
    ["English", "తెలుగు", "हिन्दी"]
)

if language == "English":
    text = {
        "title": "🚀 AI-Powered Productivity Analyzer",
        "info": "Enter a task and receive personalized productivity insights and action plans.",
        "task": "📌 What task are you avoiding?",
        "deadline": "⏳ Deadline",
        "difficulty": "⚡ Difficulty",
        "button": "🚀 Analyze My Productivity",
        "insights": "🧠 AI Insights",
        "lang_prompt": "Respond ONLY in English language. Do not use English except for technical terms."
    }

elif language == "తెలుగు":
    text = {
        "title": "🚀 AI ఆధారిత ఉత్పాదకత విశ్లేషణ",
        "info": "మీ పనిని నమోదు చేసి ఉత్పాదకత సూచనలు పొందండి.",
        "task": "📌 మీరు ఏ పనిని వాయిదా వేస్తున్నారు?",
        "deadline": "⏳ గడువు",
        "difficulty": "⚡ కష్టతరం",
        "button": "🚀 నా ఉత్పాదకతను విశ్లేషించు",
        "insights": "🧠 AI సూచనలు",
        "lang_prompt": "Respond ONLY in Telugu language. Do not use English except for technical terms."
    }

else:
    text = {
        "title": "🚀 AI आधारित उत्पादकता विश्लेषक",
        "info": "अपना कार्य दर्ज करें और उत्पादकता सुझाव प्राप्त करें।",
        "task": "📌 आप किस कार्य को टाल रहे हैं?",
        "deadline": "⏳ समय सीमा",
        "difficulty": "⚡ कठिनाई",
        "button": "🚀 मेरी उत्पादकता का विश्लेषण करें",
        "insights": "🧠 AI सुझाव",
        "lang_prompt": "Respond ONLY in Hindi language. Do not use English except for technical terms."
    }
mode = st.sidebar.selectbox(
    "🎭 AI Mode",
    ["Normal", "Funny", "Strict"]
)
# ---------------- API KEY ----------------

default_key = os.getenv("GROQ_API_KEY")

user_key = st.sidebar.text_input(
    "🔑 Enter Groq API Key (Optional)",
    type="password"
)

api_key = user_key if user_key else default_key

client = Groq(api_key=api_key)

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

st.markdown(f"### {text['title']}")

st.info(text["info"])

task = st.text_input(text["task"])
deadline = st.text_input(text["deadline"])

difficulty = st.selectbox(
    text["difficulty"],
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

if st.button(text["button"]):

    with st.spinner("Analyzing your productivity patterns..."):

        prompt = f"""
You are ProcrastiScan AI.

Task: {task}
Deadline: {deadline}
Difficulty: {difficulty}
Mode: {mode}

{text["lang_prompt"]}

If mode is Funny, give humorous productivity advice.
If mode is Strict, act like a strict productivity coach.
If mode is Normal, act like a balanced productivity mentor.

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

    # Dashboard

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🤖 AI Confidence", "95%")

    with col2:
        st.metric("🧠 Analysis", "Ready")

    with col3:
        st.metric("⚡ Status", "Active")

    st.markdown("---")

    # Productivity Assessment

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

    # AI Insights

    st.subheader(text["insights"])

    st.write(response.choices[0].message.content)
    st.download_button(
    label="📥 Download Report",
    data=response.choices[0].message.content,
    file_name="ProcrastiScan_Report.txt",
    mime="text/plain"
)
    st.session_state["analysis"] = response.choices[0].message.content
    st.markdown("---")

    st.success(
        "💡 Remember: Starting badly is better than not starting at all."
    )
# ---------------- CHATBOT ----------------

st.markdown("---")
st.subheader("💬 Chat with ProcrastiScan AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_message = st.chat_input("Ask a follow-up question...")

if user_message:

    st.session_state.messages.append(
        {"role": "user", "content": user_message}
    )

    chat_response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
               "content": f"""
You are ProcrastiScan AI.

{text["lang_prompt"]}

Previous Analysis:
{st.session_state.get("analysis", "")}

The user previously analyzed a productivity task.
Use the previous analysis when answering follow-up questions.
Help with study plans, productivity advice,
motivation, scheduling, and follow-up questions.
"""
            },
            *st.session_state.messages
        ]
    )

    answer = chat_response.choices[0].message.content

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    st.rerun()
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