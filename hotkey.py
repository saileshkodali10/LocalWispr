import threading
import keyboard

from assistant import (
    start_recording,
    stop_recording,
    run_audio_stream
)

print("===================================")
print("LocalWispr Push-To-Talk")
print("Hold Ctrl + Windows to record")
print("Release Ctrl + Windows to transcribe")
print("===================================")

audio_thread = threading.Thread(
    target=run_audio_stream,
    daemon=True
)

audio_thread.start()

recording = False


def start():
    global recording

    if not recording:
        recording = True
        start_recording()


def stop():
    global recording

    if recording:
        recording = False
        stop_recording()


keyboard.add_hotkey(
    "ctrl+windows",
    start,
    trigger_on_release=False
)

keyboard.on_release_key(
    "left windows",
    lambda e: stop()
)

keyboard.wait()