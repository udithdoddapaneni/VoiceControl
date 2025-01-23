'''
    Author: Dhruvadeep Malakar
    Email:  contact@dhruvadeep.dev

    Description: Get all information about the disk, ram, and cpu of the system.
'''

from HardwareControl.Hardware.disk_util import call_disk_util
from HardwareControl.Hardware.memory_util import get_ram_usage
from HardwareControl.Hardware.cpu_util import get_cpu_info
from HardwareControl.Hardware.cpu_util import get_cpu_usage
from text_to_voice.do import speak

class Hardware:
    def __init__(self):
        self.disk = call_disk_util
        self.ram = get_ram_usage
        self.cpu_info = get_cpu_info
        self.cpu_usage = get_cpu_usage
    
    def get_disk(self):
        info = self.disk()
        print(info)
        for (k, v) in info.items():
            speak(f"{k} is {v}")
        return info
    
    def get_ram(self):
        info = self.ram()
        print(info)
        for (k, v) in info.items():
            speak(f"{k} is {v}")
        return info
    
    def get_cpu_info(self):
        info = self.cpu_info()
        print(info)
        for (k, v) in info.items():
            speak(f"{k} is {v}")
        return info
    
    def get_cpu_usage(self):
        info = self.cpu_usage()
        print(info)
        speak(f"cpu usage is {info}") # how is it zero?
        return info
    
    def get_all(self):
        system_info = {
            "disk info": self.get_disk(),
            "ram info": self.get_ram(),
            "cpu info": self.get_cpu_info(),
            "cpu usage": self.get_cpu_usage()
        }
        return system_info