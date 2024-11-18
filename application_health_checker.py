import requests
import time
from datetime import datetime

# Define the URL of the application to monitor (Update this with your application URL or localhost)
APPLICATION_URL = "http://localhost:8000"  # Replace with your actual URL or localhost URL
EXPECTED_STATUS_CODE = 200  # Expected HTTP status code for a successful response

# Logging function to log application status into a file
def log_status(message):
    with open("application_status_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")  # Write timestamped message to the log file
    print(message)  # Print status to the console for quick feedback

# Function to check the status of the application
def check_application_status():
    try:
        response = requests.get(APPLICATION_URL, timeout=5)  # Send GET request to the application URL
        if response.status_code == EXPECTED_STATUS_CODE:  # If the response is 200, the app is UP
            log_status("Application is UP")
        else:
            log_status(f"Application is DOWN. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:  # Handle any connection-related errors
        log_status(f"Application is DOWN. Error: {e}")

# Function to continuously monitor the application health
def monitor_application_health():
    while True:
        check_application_status()  # Check the status of the application
        time.sleep(10)  # Sleep for 10 seconds before checking again

# Run the application health checker
if __name__ == "__main__":
    monitor_application_health()  # Start the health monitoring function
