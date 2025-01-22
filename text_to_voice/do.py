import pyttsx3
def speak(text,voice=3,volume=1,speed=0):
    """Function to speak out text using pyttsx3 with customized voice.
    voice = 1 for female voice,
    voice = 0 for male  voice.
    volume between 0 and 1, default 1 for full volume.
    speed - adding the speed to rate of speech
    """
    engine = pyttsx3.init()

    # Get available voices
    voices = engine.getProperty('voices')

    # Choose a voice (e.g., male or female)
    engine.setProperty('voice', voices[voice].id)  # voices[0] is usually male, voices[1] is female

    # Change the speech rate (speed of speech)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate + speed)  # Slows down the speech speed
    
    # Change the volume (0.0 to 1.0)
    engine.setProperty('volume', volume)  # Full volume

    # Speak the text
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    speak("Hello, World!")