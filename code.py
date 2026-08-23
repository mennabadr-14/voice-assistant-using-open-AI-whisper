import sounddevice as sd
import wavio
import whisper
import time
import webbrowser
import os
import sys

print("Loading Whisper AI model...")
model = whisper.load_model("base")
print("Model loaded successfully!")

SAMPLE_RATE = 16000
CHANNELS = 1
DURATION = 5

while True:

    try:
        print("\nSpeak your command...")
        print("Recording...")

        audio = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype="int16"
        )

        sd.wait()

        print("Recording finished!")
        
        filename = "record.wav"
        wavio.write(
            filename,
            audio,
            SAMPLE_RATE,
            sampwidth=2
        )

        print("Transcribing...")

        result = model.transcribe(
            filename,
            language="en",
            fp16=False
        )

        text = result["text"].strip().lower()

        print("You said:", text)
        
        if "open google" in text:
            print("Opening Google...")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in text:
            print("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")

        elif "open calculator" in text:
            print("Opening Calculator...")
            os.system("start calc")

        elif "exit" in text or "stop" in text:
            print("Goodbye!")
            break

        else:
            print("Command not recognized.")

        time.sleep(1)

    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
        break

    except Exception as e:
        print("An error occurred:", e)

if os.path.exists("record.wav"):
    os.remove("record.wav")

sys.exit()