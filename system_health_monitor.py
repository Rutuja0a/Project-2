import psutil
import time
from datetime import datetime

# Set thresholds for alerts
CPU_THRESHOLD = 80  # in percent
MEMORY_THRESHOLD = 80  # in percent
DISK_THRESHOLD = 80  # in percent

# Logging function
def log_alert(message):
    with open("system_health_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")
    print(message)

# Function to check CPU usage
def check_cpu_usage():
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage > CPU_THRESHOLD:
            log_alert(f"High CPU usage detected: {cpu_usage}%")
        else:
            print(f"CPU Usage: {cpu_usage}%")  # Print normal usage to console
    except Exception as e:
        log_alert(f"Error checking CPU usage: {e}")

# Function to check memory usage
def check_memory_usage():
    try:
        memory = psutil.virtual_memory()
        if memory.percent > MEMORY_THRESHOLD:
            log_alert(f"High Memory usage detected: {memory.percent}%")
        else:
            print(f"Memory Usage: {memory.percent}%")  # Print normal usage to console
    except Exception as e:
        log_alert(f"Error checking Memory usage: {e}")

# Function to check disk usage
def check_disk_usage():
    try:
        disk = psutil.disk_usage('/')
        if disk.percent > DISK_THRESHOLD:
            log_alert(f"Low Disk Space detected: {disk.percent}% used")
        else:
            print(f"Disk Usage: {disk.percent}%")  # Print normal usage to console
    except Exception as e:
        log_alert(f"Error checking Disk usage: {e}")

# Function to monitor system health
def monitor_system_health():
    try:
        while True:
            check_cpu_usage()
            check_memory_usage()
            check_disk_usage()
            time.sleep(5)  # Check every 5 seconds
    except KeyboardInterrupt:
        print("System monitoring stopped by user.")
    except Exception as e:
        log_alert(f"Error during monitoring: {e}")

# Run the monitor
monitor_system_health()
