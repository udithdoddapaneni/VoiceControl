## Additional things to install:

- PortAudio for using sounddevice. Help link: https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/scripts/readme-gen/templates/install_portaudio.tmpl.rst

- do the below after pip installing playwright
'''
playwright install
'''
- set your browser path in application_control/browser.py, change line 10 -> browser_path='{your path}'

To test browser_part
 run the following command in the terminal(make sure you are at /VoiceControl>)
'''
python -m application_control.browser
'''

sudo apt install espeak libespeak1 ffmpeg
sudo apt install gnome-screenshot

## Also make sure you have a good microphone