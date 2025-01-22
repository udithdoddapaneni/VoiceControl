import platform
import subprocess
import sys

def open_camera():
    """
    Opens the default camera application based on the operating system.
    Returns True if successful, False otherwise.
    """

    '''
        EIther instALL
        sudo apt-get install kamoso
        sudo apt-get install cheese
        
    '''
    system = platform.system().lower()
    
    try:
        if system == "windows":
            # Using the Windows Camera app
            subprocess.run(["start", "microsoft.windows.camera:"], shell=True)
            return True
            
        elif system == "linux":
            # Try different common camera applications
            cameras = [
                "cheese",      # GNOME's camera app
                "kamoso",      # KDE's camera app
                "guvcview",    # Simple camera viewer
                "fswebcam"     # Command-line camera tool
            ]
            
            for camera in cameras:
                try:
                    subprocess.run([camera], check=False)
                    return True
                except FileNotFoundError:
                    continue
                    
            print("No compatible camera application found. Please install one of these applications:")
            print("- cheese (GNOME)")
            print("- kamoso (KDE)")
            print("- guvcview")
            print("- fswebcam")
            return False
            
        else:
            print(f"Unsupported operating system: {system}")
            return False
            
    except Exception as e:
        print(f"Error opening camera: {str(e)}")
        return False

if __name__ == "__main__":
    success = open_camera()
    if not success:
        sys.exit(1)