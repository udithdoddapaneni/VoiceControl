from warnings import filterwarnings
filterwarnings("ignore")

import numpy as np
import whisper
import sounddevice as sd
from pynput import keyboard
from time import time as counter
from torch import cuda
from queue import Queue

from text_to_voice.do import speak
from application_control.browser import open_browser_and_search
from HardwareControl.camera import open_camera
from HardwareControl.hardware import Hardware
from HardwareControl.screenshot import screenshot

HARDWARE = Hardware()
SAMPLE_RATE = 16000
CHANNELS = 1
MAXIMUM_DURATION = 15
RECORDING = False
STREAM: sd.Stream | None = None
DEVICE = "cuda" if cuda.is_available() else "cpu"
try:
    MODEL = whisper.load_model("medium.en", DEVICE)
except:
    MODEL = whisper.load_audio("medium.en", "cpu")
START_TIME = -1

COMMANDS = [
    ("search for", open_browser_and_search),
    ("open camera", open_camera),
    ("screenshot", screenshot),
    ("ram info", HARDWARE.get_ram),
    ("disk info", HARDWARE.get_disk),
    ("cpu usage", HARDWARE.get_cpu_usage),
    ("cpu info", HARDWARE.get_cpu_info),
    ("get system info", HARDWARE.get_all)
]

def commands(transcription: str):
    for cmd, fn in COMMANDS:
        if cmd in transcription:
            if cmd == "search for":
                query = " ".join(transcription.split("search for")[1:])
                if query != "":
                    fn(query)
            else:
                fn()

def transcribe(recording):
    print("shape of the recording", recording.shape)
    result = MODEL.transcribe(
        recording,
        temperature=0,
        condition_on_previous_text=False,
        word_timestamps=True,
        # hallucination_silence_threshold=0.7,
        # no_speech_threshold=0.8
    )
    print("text:", result["text"])
    transcription = result["text"].lower()
    commands(transcription)

RECORDED_DATA = []

def callback(indata, frames, time, status): 
    global RECORDED_DATA, START_TIME, RECORDING
    RECORDED_DATA.append(indata.copy())
    if (counter() - START_TIME) >= MAXIMUM_DURATION:
        START_TIME = -1
        print("stopping recording")
        STREAM.stop()
        transcribe(np.concatenate(RECORDED_DATA, axis=0).flatten())
        RECORDED_DATA = []
        RECORDING = False

def on_press(key):
    global RECORDING, STREAM, START_TIME, RECORDED_DATA
    if key == keyboard.Key.esc:
        if STREAM:
            STREAM.stop()
            STREAM.close()
            exit(0)
        else:
            exit(0)
    if key == keyboard.Key.space:
        if not RECORDING:
            print("recording")
            RECORDING = True
            START_TIME = counter()
            STREAM = sd.InputStream(
                samplerate=SAMPLE_RATE,
                channels=CHANNELS,
                dtype=np.float32,
                callback=callback
            )
            STREAM.start()
            speak("started recording")
        else:
            print("stopping recording")
            speak("stopped recording")
            STREAM.stop()
            START_TIME = -1
            transcribe(np.concatenate(RECORDED_DATA, axis=0).flatten())
            RECORDED_DATA = []
            RECORDING = False

def recorder():
    print("start")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":  
    recorder()