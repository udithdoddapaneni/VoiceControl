import subprocess

# Run the free -h command
result = subprocess.run(['free', '-h'], capture_output=True, text=True)

# Get the output
output = result.stdout

# Parse the output
lines = output.split('\n')
headers = lines[0].split()
values = lines[1].split()

# Extract relevant values
total_memory = values[1]
used_memory = values[2]
free_memory = values[3]
shared_memory = values[4]
available_memory = values[6]

def get_ram_usage():
    return {
        "Total Memory": total_memory,
        "Used Memory": used_memory,
        "Free Memory": free_memory,
        "Shared Memory": shared_memory,
        "Available Memory": available_memory
    }