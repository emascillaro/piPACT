import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

data = pd.read_csv("raw_data.csv")

# Group all objects by distance and average their RSSI Values
means = data.groupby(["Object", "Distance"])["RSSI"].mean()

'''
Means Graph
'''

# Creates figure and axes
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

# Graphs data for each material
for material in data["Object"].unique():
    means[material].plot(ax=ax1, label=material)

# Group data by their distance and access RSSI mean
avg_strength = data.groupby(["Distance"])["RSSI"].mean()

# Plots graph
avg_strength.plot(ax=ax1, label="Average")

# Set title and label axes
ax1.set_title("RSSI Average vs Distance for Different Materials")
ax1.set_xlabel("Distance (ft)")
ax1.set_ylabel("RSSI Signal Strength")

# Puts legend in best location
fig1.legend(loc="best")

# Add gridlines & show graph
ax1.grid(b=True, which="both")
fig1.show()

# Save graph
fig1.savefig("Raw_data_means.png")

'''
Signal over 2 minutes with no barrier at 6 feet - Moving Average
'''

# Gets data for "Nothing" at 6ft and get the rolling mean
data_nothing_6ft = data[(data["Object"] == "Nothing") & (data["Distance"] == 6)]["RSSI"].rolling(window=10).mean()

# Creates figure and axes
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)

# Set title and label axes
ax2.set_title("RSSI Signal over 2 minutes with No Barrier at 6 ft (Moving Average)")
ax2.set_xlabel("Time")
ax2.set_ylabel("RSSI Signal Strength")

# Plots graph
ax2.plot(np.linspace(0, 240, len(data_nothing_6ft)), data_nothing_6ft)

# Show graph
fig2.show()

# Save graph
fig2.savefig("Nothing__6ft_variation_moving_average.png")

'''
Signal over 2 minutes with no barrier at 6 feet
'''
# Gets data for "Nothing" at 6ft and get the rolling mean
data_nothing_6ft = data[(data["Object"] == "Nothing") & (data["Distance"] == 6)]["RSSI"]

# Creates figure and axes
fig3 = plt.figure()
ax3 = fig3.add_subplot(111)

# Set title and label axes
ax3.set_title("RSSI Signal over 2 minutes with No Barrier at 6 ft")
ax3.set_xlabel("Time")
ax3.set_ylabel("RSSI Signal Strength")

# Plots graph
ax3.plot(np.linspace(0, 240, len(data_nothing_6ft)), data_nothing_6ft)

# Show graph
fig3.show()

# Save graph
fig3.savefig("Nothing__6ft_variation.png")

'''
Maxes graph
'''

# Group all objects by distance and average their RSSI Values
maxes = data.groupby(["Object", "Distance"])["RSSI"].quantile(q = 1)

# Creates figure and axes
fig4 = plt.figure()
ax4 = fig4.add_subplot(111)

# Graphs data for each material
for material in data["Object"].unique():
    maxes[material].plot(ax=ax4, label=material)

# Plot maxes
avg_strength = data.groupby(["Distance"])["RSSI"].quantile(q = 1)
avg_strength.plot(ax=ax4, label="Average")

# Set title and label axes
ax4.set_title("RSSI 100th percentile vs Distance for Different Materials")
ax4.set_xlabel("Distance (ft)")
ax4.set_ylabel("RSSI Signal Strength")

# Put legend in best location
fig4.legend(loc="best")


# Plot line at Maximum threshold
ax4.plot([1, 20],[-69, -69])

# Add gridlines & show graph
ax4.grid(b=True, which="both")
fig4.show()

# Save graph
fig4.savefig("Raw_data_100th_percentile.png")