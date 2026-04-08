import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("log.csv")

avg_speed = df["Speed(Mbps)"].mean()
min_speed = df["Speed(Mbps)"].min()
max_speed = df["Speed(Mbps)"].max()
std_dev = df["Speed(Mbps)"].std()

busiest_hour = df.loc[df["Speed(Mbps)"].idxmin(), "Hour"]

total_packets = df["Packets"].sum()

print("\n===== LOG TABLE =====\n")
print(df.to_string(index=False))

print("\n===== ANALYSIS =====\n")
print("Average Speed:", round(avg_speed, 2))
print("Min Speed:", round(min_speed, 2))
print("Max Speed:", round(max_speed, 2))
print("Std Dev:", round(std_dev, 2))
print("Total Packets:", int(total_packets))
print("Busiest Hour:", busiest_hour)

plt.plot(df["Hour"], df["Speed(Mbps)"], marker='o', label="Speed")
plt.axhline(avg_speed, linestyle='--', label="Average")

plt.xlabel("Hour")
plt.ylabel("Speed (Mbps)")
plt.title("Network Analysis with Packet Details")

plt.legend()
plt.grid()

plt.show()
