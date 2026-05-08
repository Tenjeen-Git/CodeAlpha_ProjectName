import streamlit as st
from app import get_best_answer

st.set_page_config(
    page_title="College FAQ Chatbot",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>
/* Main app background */
.stApp {
    background: linear-gradient(135deg, #f4f8ff, #e8f0ff);
    color: #1f2937;
}

/* Main content block */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

/* Header section */
.college-header {
    background: linear-gradient(90deg, #0f172a, #1d4ed8);
    padding: 28px;
    border-radius: 18px;
    color: white;
    text-align: center;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    margin-bottom: 22px;
}

.college-title {
    font-size: 40px;
    font-weight: 800;
    margin-bottom: 8px;
}

.college-subtitle {
    font-size: 18px;
    opacity: 0.95;
}

/* Section cards */
.info-card {
    background: white;
    padding: 18px;
    border-radius: 16px;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.08);
    border-left: 6px solid #1d4ed8;
    margin-bottom: 16px;
    color: #111827;
}

.info-card h3 {
    margin-top: 0;
    color: #1d4ed8;
}

.info-card p, .info-card li {
    color: #1f2937;
    font-size: 16px;
}

/* Chat bubbles */
.user-box {
    background: #dbeafe;
    color: #111827;
    padding: 14px 16px;
    border-radius: 16px 16px 4px 16px;
    margin-top: 16px;
    margin-left: 80px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.06);
    font-size: 16px;
    font-weight: 500;
}

.bot-box {
    background: #ecfdf3;
    color: #111827;
    padding: 14px 16px;
    border-radius: 16px 16px 16px 4px;
    margin-top: 12px;
    margin-right: 80px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.06);
    font-size: 16px;
    font-weight: 500;
    border-left: 5px solid #16a34a;
}

/* Input styling */
.stTextInput > div > div > input {
    background-color: white;
    color: #111827;
    border: 2px solid #93c5fd;
    border-radius: 12px;
    padding: 12px;
    font-size: 16px;
}

.stTextInput > label {
    color: #0f172a !important;
    font-weight: 700;
}

/* Button styling */
.stButton > button {
    width: 100%;
    height: 48px;
    background: linear-gradient(90deg, #1d4ed8, #2563eb);
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 17px;
    font-weight: 700;
    box-shadow: 0 6px 14px rgba(37, 99, 235, 0.25);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #0f172a;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

/* Small badge */
.badge {
    display: inline-block;
    background: #dbeafe;
    color: #1d4ed8;
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="college-header">
    <div class="college-title">🎓 College Information Portal</div>
    <div class="college-subtitle">
        Smart FAQ Assistant for Admissions, Fees, Hostel, Placements and Campus Queries
    </div>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("🏫 Campus Help Desk")
    st.write("Welcome to the college support assistant.")
    st.write("Ask questions about:")
    st.write("- Admissions")
    st.write("- Courses")
    st.write("- Fees")
    st.write("- Hostel")
    st.write("- Placements")
    st.write("- Contact Details")

    st.markdown("---")
    st.subheader("📌 Popular Questions")
    st.write("What courses are offered?")
    st.write("How can I apply for admission?")
    st.write("Is hostel available?")
    st.write("What is the fee structure?")
    st.write("How can I contact the college?")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="badge">Student Support Chatbot</div>', unsafe_allow_html=True)

    user_input = st.text_input("Enter your question")

    if st.button("Ask Question"):
        if user_input.strip() == "":
            st.warning("Please enter a question.")
        else:
            answer = get_best_answer(user_input)

            st.markdown(
                f'<div class="user-box">👩‍🎓 <b>You:</b> {user_input}</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                f'<div class="bot-box">🤖 <b>College Bot:</b> {answer}</div>',
                unsafe_allow_html=True
            )

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>📚 About the Portal</h3>
        <p>
            This assistant helps students quickly find information related to the college.
            It is designed to answer common questions in a simple and interactive way.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
        <h3>✨ Features</h3>
        <ul>
            <li>Admission help</li>
            <li>Course details</li>
            <li>Hostel information</li>
            <li>Placement support</li>
            <li>Contact guidance</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
        <h3>🎯 Tip</h3>
        <p>
            Try asking complete questions like <b>"How can I apply for admission?"</b>
            or <b>"What is the fee structure?"</b> for better answers.
        </p>
    </div>
    """, unsafe_allow_html=True)