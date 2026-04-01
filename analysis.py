analysis.py
import pandas as pd
import matplotlib.pyplot as plt

# read data
df = pd.read_csv("log.csv")

# calculations
avg_speed = df["Speed"].mean()
busiest_hour = df.loc[df["Speed"].idxmin(), "Hour"]

print("Average Speed:", round(avg_speed, 2), "Mbps")
print("Busiest Hour:", busiest_hour)

# graph
plt.plot(df["Hour"], df["Speed"], marker='o')
plt.xlabel("Hour")
plt.ylabel("Speed (Mbps)")
plt.title("Network Download Speed Analysis")
plt.grid()

plt.show()