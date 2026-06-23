# LocalWispr

Offline speech-to-text desktop application inspired by Wispr Flow.

LocalWispr allows you to dictate text anywhere on your computer using a simple push-to-talk hotkey. Everything runs locally on your machine using Whisper, with no cloud processing.

---

## Features

* Offline speech-to-text
* Fast local transcription
* Push-to-talk workflow
* Automatic text insertion
* No subscription fees
* Privacy-friendly (audio never leaves your device)

---

## Current Status

⚠️ Prototype Version

This project is currently being shared for testing and feedback.

The current version requires Python to be installed and is intended for early adopters and testers.

A standalone desktop application (.exe) is planned in future versions.

---

## Requirements

* Windows 10 or Windows 11
* Python 3.11+
* Microphone

---

## Installation

### Step 1: Install Python

Download Python from:

https://www.python.org/downloads/

During installation, ensure:

✅ Add Python to PATH

is checked.

---

### Step 2: Download LocalWispr

Clone the repository:

```bash
git clone https://github.com/saileshkodali10/LocalWispr.git
cd LocalWispr
```

Or:

* Click Code
* Download ZIP
* Extract the folder

---

### Step 3: Install Dependencies

Open Command Prompt inside the project folder.

Run:

```bash
pip install -r requirements.txt
```

Wait for installation to complete.

---

## Running LocalWispr

Run:

```bash
py hotkey.py
```

If everything loads successfully, LocalWispr will start listening for the hotkey.

---

## Usage

### Hotkey

Hold:

Ctrl + Windows Key

to start recording.

Release:

Ctrl + Windows Key

to stop recording and transcribe.

---

### Example

Speak:

"Hey Sneha, just following up on the interview."

Output:

Hey Sneha, just following up on the interview.

---

## Known Limitations

* Prototype version
* Windows only
* Requires Python installation
* No system tray icon yet
* No installer yet
* No automatic updates

---

## Feedback Requested

Please share:

### Accuracy

How accurately was your speech transcribed?

Rating: 1–10

### Speed

How responsive did it feel?

Rating: 1–10

### Ease of Use

How easy was setup and usage?

Rating: 1–10

### Bugs

Please report:

* Crashes
* Missed transcriptions
* Incorrect output
* Hotkey issues

### Feature Requests

Any features you would like to see.

---

## Roadmap

### Version 1.0

* Faster transcription
* Better punctuation
* Improved accuracy

### Version 2.0

* System tray application
* Startup on boot
* Visual status indicator

### Version 3.0

* Standalone .exe installer
* No Python required
* One-click installation

---

## Privacy

LocalWispr processes speech locally on your device.

No audio is uploaded to external servers.

---

## License

MIT License