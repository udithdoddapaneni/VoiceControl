# Run from inside the VoiceControl Directory
sudo apt install espeak libespeak1 ffmpeg
sudo apt install gnome-screenshot
sudo apt-get install portaudio19-dev python-all-dev
if [[ -d .venv ]]; then
  echo "Virtual environment found in current directory."
  source .venv/bin/activate
elif [[ -d ../.venv ]]; then
  echo "Virtual environment found in parent directory."
  # Activate the parent directory's virtual environment
  source ../.venv/bin/activate
else
  echo "Virtual environment not found. Creating virtual environment in current directory"
  python3 -m venv .venv
  source .venv/bin/activate
fi

pip install -r requirements.txt
playwright install
python3 main.py