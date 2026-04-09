import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("log.csv")

print("\n===== LOG TABLE =====\n")
print(df.to_string(index=False))

print("\nAverage Speed:", df["Speed(Mbps)"].mean())
print("Min Speed:", df["Speed(Mbps)"].min())
print("Max Speed:", df["Speed(Mbps)"].max())
print("Busiest Hour:", df.loc[df["Speed(Mbps)"].idxmin(), "Hour"])

plt.plot(df["Hour"], df["Speed(Mbps)"], marker='o')
plt.xlabel("Hour")
plt.ylabel("Speed")
plt.title("Network Performance")
plt.grid()
plt.show()