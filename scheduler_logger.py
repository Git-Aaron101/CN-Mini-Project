import csv
import time
from downloader import download_file

# create CSV with header
with open("log.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Hour", "Size", "Time", "Speed"])

print("Starting simulated 24-hour download...\n")

# simulate 24 hours
for i in range(24):
    hour = i + 1

    print(f"Running Hour {hour}...")

    size, time_taken, speed = download_file()

    print(f"Hour {hour}: {round(speed, 2)} Mbps\n")

    # save data
    with open("log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([hour, size, time_taken, speed])

    # simulate 1 hour → using 1 second delay
    time.sleep(1)

print("Simulation complete. Data saved to log.csv")