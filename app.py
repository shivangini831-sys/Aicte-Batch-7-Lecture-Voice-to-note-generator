import contextlib
import json
import os
import subprocess
import tempfile
import wave

import streamlit as st
from vosk import Model, KaldiRecognizer


# ---------------- CONFIG ---------------- #

DEFAULT_MODEL_PATH = os.getenv("VOSK_MODEL_PATH", "vosk-model")


# ---------------- VOSK MODEL ---------------- #

@st.cache_resource(show_spinner=False)
def load_vosk_model(model_path: str) -> Model:
    return Model(model_path)


# ---------------- AUDIO UTILS ---------------- #

def convert_audio_to_wav(input_path: str, wav_path: str) -> None:
    command = [
        "ffmpeg",
        "-y",
        "-i",
        input_path,
        "-ac",
        "1",
        "-ar",
        "16000",
        wav_path,
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def transcribe_audio(model: Model, wav_path: str) -> str:
    with contextlib.closing(wave.open(wav_path, "rb")) as wf:
        rec = KaldiRecognizer(model, wf.getframerate())
        rec.SetWords(True)

        text_chunks = []

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break

            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text_chunks.append(result.get("text", ""))

        final_result = json.loads(rec.FinalResult())
        text_chunks.append(final_result.get("text", ""))

    return " ".join(text_chunks).strip()


# ---------------- TEXT FORMAT ---------------- #

def format_text(text: str) -> str:
    words = text.split()
    lines = []
    line = []

    for word in words:
        line.append(word)
        if len(line) >= 12:
            lines.append(" ".join(line))
            line = []

    if line:
        lines.append(" ".join(line))

    return "\n".join(lines)


# ---------------- FEATURES ---------------- #

def generate_notes(model: Model, audio_path: str) -> str:
    with tempfile.TemporaryDirectory() as temp_dir:
        wav_path = os.path.join(temp_dir, "temp.wav")
        convert_audio_to_wav(audio_path, wav_path)
        raw_text = transcribe_audio(model, wav_path)

    if not raw_text.strip():
        return "No speech detected."

    clean_text = format_text(raw_text)
    return f"### Generated Notes\n\n{clean_text}"


def generate_quiz(transcript: str) -> str:
    if not transcript.strip():
        return "No transcript available to build a quiz."

    return (
        "### Quiz\n\n"
        "1. What is the main idea of the lecture?\n"
        "A) ...\n"
        "B) ...\n\n"
        "2. What key concept was emphasized?\n"
        "A) ...\n"
        "B) ...\n"
    )


def generate_flashcards(transcript: str) -> str:
    if not transcript.strip():
        return "No transcript available to build flashcards."

    return (
        "### Flashcards\n\n"
        "**Q:** Key concept 1\n"
        "**A:** ...\n\n"
        "**Q:** Key concept 2\n"
        "**A:** ..."
    )


# ---------------- STREAMLIT UI ---------------- #

st.set_page_config(page_title="Audio Learning Assistant", layout="wide")

st.title("Audio Learning Assistant")
st.write("Upload audio and generate notes, quizzes, or flashcards.")

uploaded_file = st.file_uploader(
    "Upload an audio file",
    type=["mp3", "wav", "m4a"],
)

audio_path = None
transcript_cache = None

if uploaded_file:
    st.success("Audio uploaded successfully.")

    temp_dir = tempfile.mkdtemp()
    audio_path = os.path.join(temp_dir, uploaded_file.name)

    with open(audio_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.audio(uploaded_file)

st.subheader("Choose Action")

col1, col2, col3 = st.columns(3)

notes_clicked = col1.button("Generate Notes")
quiz_clicked = col2.button("Generate Quiz")
flash_clicked = col3.button("Generate Flashcards")

st.subheader("Results")

if notes_clicked:
    if audio_path:
        with st.spinner("Generating notes..."):
            model = load_vosk_model(DEFAULT_MODEL_PATH)
            result = generate_notes(model, audio_path)
            st.markdown(result)
    else:
        st.warning("Please upload audio first.")

if quiz_clicked or flash_clicked:
    if audio_path:
        with st.spinner("Transcribing audio..."):
            model = load_vosk_model(DEFAULT_MODEL_PATH)

            with tempfile.TemporaryDirectory() as temp_dir:
                wav_path = os.path.join(temp_dir, "temp.wav")
                convert_audio_to_wav(audio_path, wav_path)
                transcript_cache = transcribe_audio(model, wav_path)

        if quiz_clicked:
            st.markdown(generate_quiz(transcript_cache))

        if flash_clicked:
            st.markdown(generate_flashcards(transcript_cache))
    else:
        st.warning("Please upload audio first.")

st.divider()
st.caption("Built by Lecture to Voice team")
