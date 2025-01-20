from warnings import filterwarnings
filterwarnings("ignore")

import numpy as np
import whisper
import sounddevice as sd
from pynput import keyboard
from time import time as counter

SAMPLE_RATE = 16000
CHANNELS = 1
MAXIMUM_DURATION = 15
RECORDING = False
STREAM: sd.Stream | None = None
MODEL = whisper.load_model("medium.en")
START_TIME = -1

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

RECORDED_DATA = []

def callback(indata, frames, time, status):
    global RECORDED_DATA, START_TIME, RECORDING
    RECORDED_DATA.append(indata.copy())
    if (counter() - START_TIME) >= MAXIMUM_DURATION:
        START_TIME = -1
        print("stopping recording")
        STREAM.stop()
        transcribe(np.concatenate(RECORDED_DATA, axis=0).flatten())
        RECORDING = False

def on_press(key):
    global RECORDING, STREAM, START_TIME
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
        else:
            print("stopping recording")
            STREAM.stop()
            START_TIME = -1
            transcribe(np.concatenate(RECORDED_DATA, axis=0).flatten())
            RECORDING = False

def recorder():
    print("start")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    recorder()