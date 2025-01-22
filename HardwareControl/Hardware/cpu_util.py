'''
    Author:    Dhruvadeep Malakar
    Email:     contact@dhruvadeep.dev

    Description: Get all information about the cpu of the system.
    Error:       Accurate CPU usage is not displayed.

'''

import psutil
def get_cpu_info():
    cpu_info = {}
    with open("/proc/cpuinfo", "r") as f:
        for line in f:
            if line.strip():
                if ":" in line:
                    key, value = line.split(":", 1)
                    key = key.strip()
                    value = value.strip()
                    if key == "model name":
                        cpu_info["CPU Model"] = value
                    elif key == "cpu MHz":
                        cpu_info["CPU MHz"] = value
                    elif key == "cache size":
                        cpu_info["Cache Size"] = value
                    elif key == "cpu cores":
                        cpu_info["Physical Cores"] = value
                    elif key == "siblings":
                        cpu_info["Total Cores"] = value
                    # Add more keys if needed
                    # elif key == "cpu usage":
                    #     cpu_info["Total CPU Usage"] = value

    return cpu_info

def get_cpu_usage():
    return f"{psutil.cpu_percent(interval=None)}%"
