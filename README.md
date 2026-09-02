# 🎙️ Voice Command Assistant

## 📌 Overview

The **Voice Command Assistant** is a Python-based application that uses **Whisper AI** for speech recognition.

The program records the user's voice, converts the speech into text, and then performs specific actions depending on the detected command.

---

## ✨ Features

* 🎙️ Voice recording
* 🤖 Speech-to-text using Whisper AI
* 🌐 Open Google using a voice command
* ▶️ Open YouTube using a voice command
* 🧮 Open the Calculator using a voice command
* 🛑 Stop the program using a voice command
* 💻 Display recognized commands in the terminal

---

## 🧰 Technologies & Libraries

* **Python 3**
* **OpenAI Whisper**
* **SoundDevice**
* **WAVIO**
* **Webbrowser**
* **OS**
* **Time**

---

## 📚 Required Libraries

The project uses the following Python libraries:

```text
sounddevice
wavio
whisper
```

Install them using:

```bash
pip install sounddevice wavio openai-whisper
```

> Depending on your system, additional audio dependencies may be required for `sounddevice`.

---

## ⚙️ How It Works

1. The Whisper AI model is loaded when the program starts.
2. The program waits for the user to speak a command.
3. It records the user's voice for **5 seconds**.
4. The recorded audio is temporarily saved as a WAV file.
5. Whisper processes the recording and converts it into text.
6. The recognized text is checked against the available commands.
7. The corresponding action is executed.
8. The program continues listening until the user says **"exit"** or **"stop"**.

---

## 🎤 Available Voice Commands

| Voice Command     | Action                       |
| ----------------- | ---------------------------- |
| `open Google`     | Opens Google in the browser  |
| `open YouTube`    | Opens YouTube in the browser |
| `open calculator` | Opens the system calculator  |
| `exit`            | Stops the program            |
| `stop`            | Stops the program            |

---

## 🧠 System Workflow

```text
Start
  │
  ▼
Load Whisper AI Model
  │
  ▼
Record Voice
  │
  ▼
Save Audio
  │
  ▼
Whisper Transcription
  │
  ▼
Recognize Command
  │
  ├── Open Google ──────► Browser
  │
  ├── Open YouTube ─────► Browser
  │
  ├── Open Calculator ──► Calculator
  │
  ├── Exit / Stop ──────► End Program
  │
  └── Unknown Command ──► Try Again
```

---

## ▶️ Running the Project

Run the Python file using:

```bash
python main.py
```

Make sure your computer has a working **microphone** and an internet connection if required by the Whisper model setup.

---

## 🎯 Project Purpose

This project demonstrates how **speech recognition and Python automation** can be combined to create a simple voice-controlled assistant.

It is a useful beginner project for learning about:

* Speech recognition
* AI models
* Audio recording
* Python automation
* Voice-controlled applications

---

## 🚀 Future Improvements

Possible improvements include:

* Add more voice commands.
* Control music using voice.
* Search the web using voice commands.
* Add a graphical user interface.
* Add support for multiple languages.
* Control smart-home or IoT devices using voice.
* Save command history in a text file.

---

## 📄 License

This project was created for **educational purposes** and can be modified and improved for learning and experimentation.
