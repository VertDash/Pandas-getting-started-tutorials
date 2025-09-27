import pandas as pd
import matplotlib.pyplot as plt

# Read air quality data
air_quality = pd.read_csv(
    "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/air_quality_no2.csv",
    index_col=0, parse_dates=True
)

# Create line plot
air_quality.plot()
plt.show()

# Create scatter plot
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()

# Create box plot
air_quality.plot.box()
plt.show()

# Save line plot to file
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.savefig("air_quality_scatter.png")
plt.close()

# Plot on existing axis
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.plot.area(ax=axs)
axs.set_ylabel("NO2 concentration")
plt.show()