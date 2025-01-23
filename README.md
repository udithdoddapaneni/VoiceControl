## How to run:

- In terminal navigate to the current directory
- bash run.sh

The above will install dependencies if any and run the program.
You may see some or warnings, just ignore them and wait for "start" to appear.
Then spacebar for starting and stopping the voice recording.


Now these are the following voice commands and their functionalities that we added:

"take screenshot", "take a screenshot" : takes a screen shot
"show ram info", "get ram info", "show ram usage", "get ram usage": shows ram info and usage
"show disk info", "get disk info", "show disk usage", "get disk usage": shows disk info and usage
"show cpu usage", "get cpu usage": shows cpu usage
"show cpu info", "get cpu info": shows cpu info
"show system info", "get system info", "show hardware info", "get hardware info": show disk info, cpu usage, ram info...etc
"open browser": opens a browser
"open camera": opens camera
"search for", "search", "bing": searches the given query on something on bing

Alternatively on subsequent runs when you have already installed all the dependencies you can just do:
source .venv/bin/activate
python3 main.py

## Dependencies:

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
sudo apt-get install portaudio19-dev python-all-dev
## Also make sure you have a good microphone

## Team members:
- 142201012: Doddapaneni Udith
- 142201014: Vishnu Shreeram
- 142201026: Dhruvadeep

## Link for demo: https://drive.google.com/drive/folders/1qiPbUMA_2uULneZozGfOD2jGz2QPm6Gl?usp=sharing