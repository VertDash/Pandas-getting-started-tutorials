import pandas as pd
import matplotlib.pyplot as plt

# Read air quality data
air_quality = pd.read_csv(
    "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/air_quality_no2.csv"
)

# The datetime column is already named correctly, just convert it
air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])

# Set datetime column as index
air_quality = air_quality.set_index("datetime")

# Check the index
print(air_quality.index)

# Calculate and print the time range
print(air_quality.index.min())
print(air_quality.index.max())

# Print time span
print(air_quality.index.max() - air_quality.index.min())

# Add month column
air_quality["month"] = air_quality.index.month

# Melt the dataframe to get it in the format needed
air_quality_melted = pd.melt(
    air_quality.reset_index(),
    id_vars=['datetime', 'month'],
    value_vars=['station_antwerp', 'station_paris', 'station_london'],
    var_name='location',
    value_name='value'
)
air_quality_melted = air_quality_melted.set_index('datetime')

# Calculate average by weekday and station
weekday_avg = air_quality_melted.groupby(
    [air_quality_melted.index.weekday, "location"])["value"].mean()
print(weekday_avg)

# Plot hourly values
fig, ax = plt.subplots(figsize=(10, 5))
air_quality_melted.groupby(air_quality_melted.index.hour)["value"].mean().plot(
    kind="bar",
    rot=0,
    ax=ax
)
plt.xlabel("Hour of the day")
plt.ylabel("$NO_2 (µg/m^3)$")
plt.show()

# Create pivoted DataFrame
no2 = air_quality_melted.pivot(columns="location", values="value")
print(no2.head())

# Access time information 
print(no2.index.year)
print(no2.index.weekday)

# Plot time range slice
no2["2019-05-20":"2019-05-21"].plot()
plt.show()

# Monthly maximum values
monthly_max = no2.resample("M").max()
print(monthly_max)

# Check the frequency 
print(monthly_max.index.freq)

# Plot daily means
no2.resample("D").mean().plot(style="-o", figsize=(10, 5))
plt.show()