# log_file_analyzer.py

from collections import Counter

# Define log file path
LOG_FILE_PATH = "/Users/rutujaahire/Desktop/monitoring_scripts/access.log"


# Function to analyze log file
def analyze_log():
    with open(LOG_FILE_PATH, "r") as log_file:
        lines = log_file.readlines()

    status_404_count = 0
    page_requests = Counter()
    ip_requests = Counter()

    for line in lines:
        parts = line.split()
        if len(parts) > 8:
            ip = parts[0]
            request = parts[6]
            status = parts[8]

            # Count 404 errors
            if status == "404":
                status_404_count += 1

            # Track page requests and IPs
            page_requests[request] += 1
            ip_requests[ip] += 1

    # Output summary
    print(f"Total 404 Errors: {status_404_count}")
    print("Top 5 Requested Pages:")
    for page, count in page_requests.most_common(5):
        print(f"{page}: {count} requests")

    print("Top 5 IPs by Request Count:")
    for ip, count in ip_requests.most_common(5):
        print(f"{ip}: {count} requests")

# Run the log file analyzer
analyze_log()
