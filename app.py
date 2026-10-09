import os
import streamlit as st
from google import genai
from pypdf import PdfReader

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="StudyMate AI",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# Title
# -----------------------------
st.title("🤖 StudyMate AI")
st.caption("AI-powered study assistant for college students")

# -----------------------------
# API Key
# -----------------------------
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ Gemini API key not found.")
    st.stop()

client = genai.Client(api_key=api_key)

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""

if "pdf_name" not in st.session_state:
    st.session_state.pdf_name = ""

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.header("📚 StudyMate")

    # Subject selection
    subject = st.selectbox(
        "Choose a subject",
        [
            "General",
            "Python",
            "Java",
            "Data Structures",
            "Cyber Security",
            "Database",
            "Computer Networks"
        ]
    )

    st.divider()

    # -----------------------------
    # Voice Question
    # -----------------------------
    st.subheader("🎤 Voice Question")

    audio = st.audio_input(
        "Record your question"
    )

    if audio:

        st.audio(audio)

        if st.button("🤖 Ask Gemini with Voice"):

            try:

                with st.spinner(
                    "🎧 Gemini is listening..."
                ):

                    audio_bytes = audio.getvalue()

                    # Send audio directly to Gemini
                    response = client.models.generate_content(
                        model="gemini-3.5-flash-lite",
                        contents=[
                            """
You are StudyMate AI, a college study assistant.

Listen to the student's audio question.

Understand the question and answer it clearly.

Rules:
- Use simple language.
- Give examples when useful.
- For programming questions, provide code.
- Explain difficult concepts step-by-step.
- Answer only what the student is asking.
""",
                            genai.types.Part.from_bytes(
                                data=audio_bytes,
                                mime_type="audio/wav"
                            )
                        ]
                    )

                    voice_answer = response.text

                # Display answer
                st.success("✅ Voice question processed!")

                st.markdown("### 🤖 StudyMate")

                st.markdown(voice_answer)

                # Save to chat
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": voice_answer
                })

            except Exception as e:

                st.error("❌ Voice processing error")
                st.code(str(e))

    st.divider()

    # -----------------------------
    # PDF Upload
    # -----------------------------
    st.subheader("📄 Study PDF")

    uploaded_file = st.file_uploader(
        "Upload your notes",
        type=["pdf"]
    )

    if uploaded_file:

        if st.session_state.pdf_name != uploaded_file.name:

            reader = PdfReader(uploaded_file)

            text = ""

            for page in reader.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

            st.session_state.pdf_text = text
            st.session_state.pdf_name = uploaded_file.name

        st.success(
            f"✅ {uploaded_file.name} loaded"
        )

    st.divider()

    # -----------------------------
    # Clear Chat
    # -----------------------------
    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []
        st.session_state.pdf_text = ""
        st.session_state.pdf_name = ""

        st.rerun()

    st.divider()

    # -----------------------------
    # About
    # -----------------------------
    st.write("### About")

    st.write(
        "StudyMate AI helps college students "
        "understand technical subjects, ask "
        "questions using voice, and study "
        "uploaded PDF notes."
    )

# -----------------------------
# Display Chat History
# -----------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# Text Chat Input
# -----------------------------
prompt = st.chat_input(
    "Ask your question..."
)

if prompt:

    # Display user question
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # AI response
    with st.chat_message("assistant"):

        try:

            with st.spinner(
                "🤖 StudyMate is thinking..."
            ):

                # -----------------------------
                # PDF-based question
                # -----------------------------
                if st.session_state.pdf_text:

                    instruction = f"""
You are StudyMate AI, a college study assistant.

The student has uploaded a PDF.

Selected subject:
{subject}

Answer the student's question using the
uploaded PDF whenever possible.

If the answer is not present in the PDF,
clearly say that the information was not
found in the uploaded document.

Use simple language and examples when useful.

PDF CONTENT:
{st.session_state.pdf_text}

STUDENT QUESTION:
{prompt}
"""

                # -----------------------------
                # Normal question
                # -----------------------------
                else:

                    instruction = f"""
You are StudyMate AI, a college study assistant.

Selected subject:
{subject}

Answer the student's question clearly.

Rules:
- Use simple language.
- Give examples when useful.
- For programming questions, provide code.
- Explain difficult concepts step-by-step.

Student question:
{prompt}
"""

                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=instruction
                )

                answer = response.text

                st.markdown(answer)

                # Save answer
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

        except Exception as e:

            st.error("❌ Gemini API Error")
            st.code(str(e))