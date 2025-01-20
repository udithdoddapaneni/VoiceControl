import numpy as np
import whisper
import sounddevice as sd
import time

SAMPLE_RATE = 16000
CHANNELS = 1

result = sd.rec(frames=3,samplerate=SAMPLE_RATE, channels=CHANNELS, dtype=np.float32)


