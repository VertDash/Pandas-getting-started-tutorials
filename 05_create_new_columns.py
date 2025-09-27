import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    # Load the air quality NO2 data with datetime index
    url = "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/air_quality_no2.csv"
    print("Loading air quality data with datetime index...")
    air = pd.read_csv(url, parse_dates=["datetime"], index_col="datetime")
    print("Head of data:")
    print(air.head(), "\n")

    
    conv = 1.882
    air["london_mg_per_cubic"] = air["station_london"] * conv
    print("Added column 'london_mg_per_cubic':")
    print(air[["station_london", "london_mg_per_cubic"]].head(), "\n")

    # compute a ratio: Paris / Antwerp
    air["ratio_paris_antwerp"] = air["station_paris"] / air["station_antwerp"]
    print("Added column 'ratio_paris_antwerp':")
    print(air[["station_paris", "station_antwerp", "ratio_paris_antwerp"]].head(), "\n")

    # Rename columns 
    rename_map = {
        "station_antwerp": "ANTW",
        "station_paris": "PAR",
        "station_london": "LOND"
    }
    air_renamed = air.rename(columns=rename_map)
    print("After renaming columns:")
    print(air_renamed.head(), "\n")

    # rename can accept a function
    air_lower = air_renamed.rename(columns=str.lower)
    print("After renaming via str.lower (all to lowercase):")
    print(air_lower.head(), "\n")

    # plot a column to see the new values
    out_dir = "examples_output"
    os.makedirs(out_dir, exist_ok=True)

    plt.figure(figsize=(8, 4))
    if "london_mg_per_cubic" in air.columns:
        air["london_mg_per_cubic"].plot(title="London in mg/m³ (derived)")
        plt.ylabel("mg/m³ (converted)")
        plt.tight_layout()
        fn = os.path.join(out_dir, "05_london_mg_plot.png")
        plt.savefig(fn)
        plt.close()
        print("Saved plot of converted London NO2 to:", fn)
    else:
        print("london_mg_per_cubic not found — skipping plot.")

if __name__ == "__main__":
    main()