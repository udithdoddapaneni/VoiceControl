#!/usr/bin/env python3

import datetime
import pyscreenshot as ImageGrab  # pip install pyscreenshot

def capture_screenshot():
    # Get timestamp in YYYYmmdd_HHMMSS format
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Construct file name
    filename = f"screenshot_{timestamp}.png"
    
    # Capture the entire screen
    image = ImageGrab.grab()
    
    # Save in the same directory as this Python file
    image.save(filename)
    print(f"Screenshot saved as {filename}")

if __name__ == "__main__":
    capture_screenshot()
