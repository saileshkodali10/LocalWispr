# LocalWispr

A lightweight offline speech-to-text application inspired by Wispr Flow.

## Features

- Offline transcription using Whisper
- Push-to-talk recording
- Automatic text cleanup
- Auto-paste into any application
- Fast local processing
- No API costs
- No internet required

## Requirements

- Windows 10/11
- Python 3.11+
- Microphone

## Installation

Clone the repository:

```bash
git clone https://github.com/saileshkodali10/LocalWispr.git
cd LocalWispr
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
py -3.13 hotkey.py
```

## Usage

1. Launch LocalWispr
2. Hold Ctrl + Win
3. Speak
4. Release keys
5. Text is automatically transcribed and pasted

## Project Structure

assistant.py      # Main orchestration
record.py         # Audio recording
transcribe.py     # Whisper transcription
fillers.py        # Text cleanup
hotkey.py         # Push-to-talk controls

## Roadmap

- System tray application
- Custom icon
- Startup on boot
- Settings page
- Multiple language support
- Packaged EXE installer
## License

MIT
