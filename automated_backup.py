import os
import tarfile
from datetime import datetime

# Configuration for local directory and backup location
SOURCE_DIR = "/Users/rutujaahire/Desktop/01_html/Homepage/about.html"  # Update with the directory you want to back up
BACKUP_DIR = "/Users/rutujaahire/Desktop/01_html/"  # Directory where backups will be stored

# Log file to store backup status
LOG_FILE = "backup_log.txt"

# Function to log backup status
def log_status(message):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")
    print(message)

# Function to perform local backup by compressing the directory
def perform_local_backup():
    if not os.path.exists(SOURCE_DIR):
        log_status(f"Source directory does not exist: {SOURCE_DIR}")
        return

    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)  # Create the backup directory if it doesn't exist

    backup_filename = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.tar.gz"
    backup_path = os.path.join(BACKUP_DIR, backup_filename)

    try:
        with tarfile.open(backup_path, "w:gz") as tar:
            tar.add(SOURCE_DIR, arcname=os.path.basename(SOURCE_DIR))
        log_status(f"Backup completed successfully. Backup file: {backup_path}")
    except Exception as e:
        log_status(f"Backup failed: {e}")

# Run the backup
perform_local_backup()
