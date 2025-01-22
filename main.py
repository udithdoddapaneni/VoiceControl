from voice_to_text.converter import recorder
from text_to_voice.do import speak
from application_control.browser import open_browser_and_search
from HardwareControl.camera import open_camera
from HardwareControl.hardware import Hardware
from HardwareControl.screenshot import screenshot

def sample():
    print("hello")

def main():
    recorder()


if __name__ == "__main__":
    main()