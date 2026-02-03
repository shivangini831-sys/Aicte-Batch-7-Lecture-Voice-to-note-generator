import streamlit as st
import tempfile
import os

st.set_page_config(page_title="Audio Learning Assistant", layout="wide")

st.title("🎧 Audio Learning Assistant")
st.write("Upload audio and generate notes, quizzes, or flashcards.")

uploaded_file = st.file_uploader(
    "Upload an audio file",
    type=["mp3", "wav", "m4a"]
)

audio_path = None
# Handle file upload

if uploaded_file:
    st.success("Audio uploaded successfully!")

    temp_dir = tempfile.mkdtemp()
    audio_path = os.path.join(temp_dir, uploaded_file.name)

    with open(audio_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.audio(uploaded_file)

st.subheader("Choose Action")

col1, col2, col3 = st.columns(3)

notes_clicked = col1.button("📝 Generate Notes")
quiz_clicked = col2.button("❓ Generate Quiz")
flash_clicked = col3.button("🧠 Generate Flashcards")

def generate_notes(audio_path):
    return "### Generated Notes\n\n- Point 1\n- Point 2\n- Summary..."

def generate_quiz(audio_path):
    return """
### Quiz

1. Question one?
A) Option A  
B) Option B  

2. Question two?
A) Option A  
B) Option B  
"""

def generate_flashcards(audio_path):
    return """
### Flashcards

**Q:** Concept 1  
**A:** Explanation

**Q:** Concept 2  
**A:** Explanation
"""

st.subheader("Results")

if notes_clicked:
    if audio_path:
        with st.spinner("Generating notes..."):
            result = generate_notes(audio_path)
        st.markdown(result)
    else:
        st.warning("Please upload audio first.")

if quiz_clicked:
    if audio_path:
        with st.spinner("Generating quiz..."):
            result = generate_quiz(audio_path)
        st.markdown(result)
    else:
        st.warning("Please upload audio first.")

if flash_clicked:
    if audio_path:
        with st.spinner("Generating flashcards..."):
            result = generate_flashcards(audio_path)
        st.markdown(result)
    else:
        st.warning("Please upload audio first.")

st.divider()
st.caption("Built with ❤️ By Leacture to voice team")
