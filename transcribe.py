from faster_whisper import WhisperModel

model = WhisperModel(
"small.en",
device="cpu",
compute_type="int8"
)

segments, info = model.transcribe(
"recording.wav",
beam_size=1
)

transcript = " ".join(
segment.text.strip()
for segment in segments
)

print(transcript)
