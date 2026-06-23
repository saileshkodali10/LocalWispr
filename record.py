from scipy.io.wavfile import write
import sounddevice as sd

fs = 16000
seconds = 3

print("Recording...")

audio = sd.rec(
    int(seconds * fs),
    samplerate=fs,
    channels=1
)

sd.wait()

write("recording.wav", fs, audio)

print("Saved as recording.wav")