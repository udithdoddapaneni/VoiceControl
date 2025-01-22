import pyautogui
from datetime import datetime


def screenshot():
    # Generate a timestamp for the filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{timestamp}.png"

    # Take a screenshot
    screenshot = pyautogui.screenshot()

    # Save the screenshot
    screenshot.save(filename)

    print(f"Screenshot saved as {filename}")
