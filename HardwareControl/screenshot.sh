#!/usr/bin/env bash

# Requires either 'scrot' or 'import' (from the ImageMagick suite) installed.
# Example using scrot:

timestamp=$(date +%Y%m%d_%H%M%S)
filename="screenshot_${timestamp}.png"

# Capture the entire screen
scrot "$filename"

echo "Screenshot saved as $filename"
