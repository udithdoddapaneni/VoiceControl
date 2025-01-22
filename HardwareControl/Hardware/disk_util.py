'''
    Author:  Dhruvadeep Malakar
    Email:   contact@dhruvadeep.dev

    Description: This script is used to get the disk information of the system. Returns the total, used, and free space of the disk in a human-readable format.
    Annotations: B, KB, MB, GB, TB
'''

import shutil

def get_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)
    return total, used, free

def format_size(bytes_size):
    # Convert bytes to a more human-readable format (e.g., KB, MB, GB, TB)
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024

def call_disk_util():
    path = "/"
    total, used, free = get_disk_usage(path)

    return {
        "Total Space": format_size(total),
        "Used Space": format_size(used),
        "Free Space": format_size(free)
    }