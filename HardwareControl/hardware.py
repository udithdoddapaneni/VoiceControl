'''
    Author: Dhruvadeep Malakar
    Email:  contact@dhruvadeep.dev

    Description: Get all information about the disk, ram, and cpu of the system.
'''

from Hardware.disk_util import call_disk_util
from Hardware.memory_util import get_ram_usage
from Hardware.cpu_util import get_cpu_info
from Hardware.cpu_util import get_cpu_usage

class Hardware:
    def __init__(self):
        self.disk = call_disk_util()
        self.ram = get_ram_usage()
        self.cpu_info = get_cpu_info()
        self.cpu_usage = get_cpu_usage()
    
    def get_disk(self):
        return self.disk
    
    def get_ram(self):
        return self.ram
    
    def get_cpu_info(self):
        return self.cpu_info
    
    def get_cpu_usage(self):
        return self.cpu_usage
    
    def get_all(self):
        return {
            "disk": self.disk,
            "ram": self.ram,
            "cpu_info": self.cpu_info,
            "cpu_usage": self.cpu_usage
        }