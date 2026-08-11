# Smart Voice Assistance & Calculator

A Python-based desktop smart voice assistant ("Rio") and desktop GUI calculator built with Tkinter.

## Features

- **Smart Voice Assistant (Rio)**: Voice-activated operations including note-taking, browser search, weather lookups, screenshots, jokes, system shutdown/restart, and a fitness chatbot helper.
- **GUI Calculator**: Clean desktop calculator supporting arithmetic calculations with full keyboard entry capabilities and error safety.
- **Cross-Platform Compatibility**: Automatically runs on Windows and macOS.

## Prerequisites

Ensure you have Python 3 installed. Install package dependencies:
```bash
pip install pyautogui pyttsx3 SpeechRecognition wikipedia pyjokes beautifulsoup4 Pillow requests
```
*Note: Some voice features require PyAudio.*

## How to Run

- **Calculator**:
  ```bash
  python main.py
  ```

- **Voice Assistant**:
  ```bash
  python Rio_startpart.py
  ```

## Running Tests

To run the calculator test suite:
```bash
python -m unittest test_calc.py
```
