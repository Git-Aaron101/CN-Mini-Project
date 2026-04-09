import csv
import time
from downloader import download_file

with open("log.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Hour", "Size(Bytes)", "Time(s)", "Speed(Mbps)", "Packets"])

print("Simulating 24 hours...\n")

for i in range(24):
    hour = i + 1

    size, time_taken, speed, packets = download_file()

    print(f"Hour {hour}: {round(speed,2)} Mbps")

    with open("log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([hour, size, time_taken, speed, packets])

    time.sleep(1)  # 1 sec = 1 hour

print("Logging complete")










