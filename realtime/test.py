import sounddevice as sd
import numpy as np
import whisper
import time

# Initialize Whisper model
model = whisper.load_model("medium.en")
model.eval()

# Audio parameters
SAMPLE_RATE = 16000
BLOCK_TIME = 3.5
OVERLAP_TIME = 2.5
BLOCK_SIZE = int(SAMPLE_RATE*BLOCK_TIME)
OVERLAP = int(SAMPLE_RATE*OVERLAP_TIME)

# Initialize variables for audio stream and buffering
buffer = np.zeros(BLOCK_SIZE * 2)  # Buffer for storing overlapping audio

# Function to record audio and feed to Whisper for transcription
def callback(indata, frames, time, status):
    global buffer
    if status:
        print(status, flush=True)
    # Append new data to buffer
    buffer = np.roll(buffer, -frames)
    buffer[-frames:] = indata[:, 0]  # Assuming mono audio (single channel)
    
    # Process audio in chunks with overlap
    if len(buffer) >= BLOCK_SIZE:
        chunk = buffer[:BLOCK_SIZE].astype(np.float32)
        # Feed chunk to Whisper model
        result = model.transcribe(np.array(chunk).flatten(), temperature=0, condition_on_previous_text=False, word_timestamps=True, hallucination_silence_threshold=0.9, no_speech_threshold=0.8)
        print("Transcription:", result["text"])

# Start audio stream
print("Starting real-time streaming...")
with sd.InputStream(callback=callback, channels=1, samplerate=SAMPLE_RATE, blocksize=BLOCK_SIZE):
    while True:
        time.sleep(0.1)  # Allow continuous processing