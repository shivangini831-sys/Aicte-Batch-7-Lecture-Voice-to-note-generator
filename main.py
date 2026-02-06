import os
import json
import subprocess
import wave
import contextlib
from vosk import Model, KaldiRecognizer

# ---------------- CONFIG ----------------
DATASET_DIR = "dataset"
OUTPUT_DIR = "output"
MODEL_PATH = "vosk-model"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------------- LOAD MODEL ----------------
print("Loading Vosk model...")
model = Model(MODEL_PATH)
print("Model loaded successfully.\n")

# ---------------- UTIL FUNCTIONS ----------------
def convert_mp3_to_wav(mp3_path, wav_path):
    command = [
        "ffmpeg", "-y",
        "-i", mp3_path,
        "-ac", "1",
        "-ar", "16000",
        wav_path
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def transcribe_audio(wav_path):
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

    full_text = " ".join(text_chunks).strip()
    return full_text


def format_text(text):
    # Break long text into readable sentences
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


# ---------------- MAIN PROCESS ----------------
print("Lecture Voice-to-Notes Generator\n")

for file in os.listdir(DATASET_DIR):
    if not file.lower().endswith(".mp3"):
        continue

    print(f"🎧 Processing: {file}")

    mp3_path = os.path.join(DATASET_DIR, file)
    wav_path = os.path.join(DATASET_DIR, "temp.wav")

    print("   🔄 Extracting audio...")
    convert_mp3_to_wav(mp3_path, wav_path)

    print("   📝 Transcribing...")
    raw_text = transcribe_audio(wav_path)

    if not raw_text.strip():
        print("   ⚠️ No speech detected, skipping\n")
        continue

    clean_text = format_text(raw_text)

    output_file = os.path.join(
        OUTPUT_DIR,
        os.path.splitext(file)[0] + ".txt"
    )

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(clean_text)

    print(f"   ✅ Saved: {output_file}\n")

    os.remove(wav_path)

print("🎉 All files processed successfully!")
