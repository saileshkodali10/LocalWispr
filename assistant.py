import time
import threading

import keyboard
import numpy as np
import pyperclip
import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

from fillers import clean_text

FS = 16000

print("Loading Whisper model...")

model = WhisperModel(
    "small.en",
    device="cpu",
    compute_type="int8"
)

print("Whisper loaded successfully!")

recording = False
audio_chunks = []


def audio_callback(indata, frames, time_info, status):
    global recording, audio_chunks

    if recording:
        audio_chunks.append(indata.copy())


def start_recording():
    global recording, audio_chunks

    audio_chunks = []
    recording = True

    print("\nRecording started...")


def stop_recording():
    global recording, audio_chunks

    recording = False

    print("Recording stopped.")

    if len(audio_chunks) == 0:
        print("No audio captured.")
        return

    audio = np.concatenate(audio_chunks, axis=0)

    write(
        "recording.wav",
        FS,
        audio
    )

    start_time = time.time()

    print("Transcribing...")

    segments, info = model.transcribe(
        "recording.wav",
        beam_size=5
    )

    transcript = " ".join(
        segment.text.strip()
        for segment in segments
    )

    cleaned = clean_text(transcript)

    print("\nFinal Text:\n")
    print(cleaned)

    pyperclip.copy(cleaned)

    time.sleep(0.3)

    keyboard.press_and_release("ctrl+v")

    print(
        f"\nProcessing time: {time.time() - start_time:.2f} sec"
    )


def run_audio_stream():
    with sd.InputStream(
        samplerate=FS,
        channels=1,
        callback=audio_callback
    ):
        while True:
            time.sleep(0.1)