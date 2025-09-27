import pandas as pd

def main():
    # Load both datasets from the tutorial
    url = "https://github.com/pandas-dev/pandas/raw/main/doc/data/titanic.csv"
    titanic = pd.read_csv(url)
    
    air_quality_url = "https://github.com/pandas-dev/pandas/raw/main/doc/data/air_quality_long.csv"
    air_quality = pd.read_csv(air_quality_url, index_col="date.utc", parse_dates=True)
    
    print("=== Original Data Shape ===")
    print(f"Shape: {titanic.shape}")
    print(titanic.head(3), "\n")

    # Example: pivot table (average Fare by Pclass and Sex)
    pivoted = titanic.pivot_table(values="Fare", index="Pclass", columns="Sex", aggfunc="mean")
    print("=== Pivot table (mean Fare by Pclass x Sex) ===")
    print(pivoted, "\n")

    # melt: make wide -> long
    sample = titanic.loc[:9, ["PassengerId", "Name", "Age", "Fare"]]
    print("=== Original sample (wide format) ===")
    print(sample, "\n")
    
    melted = sample.melt(id_vars=["PassengerId", "Name"], value_vars=["Age", "Fare"],
                         var_name="variable", value_name="value")
    print("=== Melted sample (long format) ===")
    print(melted.head(10), "\n")

    # stack / unstack example with groupby
    grp = titanic.groupby(["Sex", "Pclass"])["Fare"].mean()
    print("=== Groupby result (multiindex Series) ===")
    print(grp, "\n")
    
    unstacked = grp.unstack()
    print("=== Unstacked into DataFrame ===")
    print(unstacked, "\n")
    
    # Show how to stack it back
    stacked_back = unstacked.stack()
    print("=== Stacked back to Series ===")
    print(stacked_back, "\n")
    
    # Additional pivot example - survival rate by class and embarkation
    survival_pivot = titanic.pivot_table(
        values="Survived", 
        index="Pclass", 
        columns="Embarked", 
        aggfunc="mean",
        fill_value=0
    )
    print("=== Survival rate by Class and Embarkation ===")
    print(survival_pivot, "\n")
    
    # Cross-tabulation example
    crosstab = pd.crosstab(titanic["Pclass"], titanic["Survived"], margins=True)
    print("=== Cross-tabulation: Class vs Survived ===")
    print(crosstab, "\n")
    
    # Wide to long with multiple value columns
    sample_multi = titanic.loc[:5, ["PassengerId", "Age", "Fare", "SibSp", "Parch"]]
    melted_multi = pd.melt(
        sample_multi, 
        id_vars=["PassengerId"], 
        value_vars=["Age", "Fare", "SibSp", "Parch"],
        var_name="Measurement", 
        value_name="Value"
    )
    print("=== Multi-column melt ===")
    print(melted_multi.head(10), "\n")
    
    # Demonstrate pivot (not pivot_table) - reshape without aggregation
    # First create a simple dataset
    simple_data = pd.DataFrame({
        'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
        'Variable': ['Temp', 'Humidity', 'Temp', 'Humidity'],
        'Value': [20, 65, 22, 70]
    })
    print("=== Simple data for pivot example ===")
    print(simple_data, "\n")
    
    pivoted_simple = simple_data.pivot(index='Date', columns='Variable', values='Value')
    print("=== Pivoted simple data (no aggregation) ===")
    print(pivoted_simple, "\n")
    
    # === AIR QUALITY DATA EXAMPLES FROM TUTORIAL ===
    print("=== Air Quality Data Examples ===")
    print("Air quality data shape:", air_quality.shape)
    print(air_quality.head(), "\n")
    
    # Long to wide format using air quality data
    no2 = air_quality[air_quality["parameter"] == "no2"]
    no2_subset = no2.sort_index().groupby(["location"]).head(2)
    print("=== NO2 subset (long format) ===")
    print(no2_subset, "\n")
    
    # Pivot: long to wide
    no2_pivoted = no2_subset.pivot(columns="location", values="value")
    print("=== NO2 pivoted (wide format) ===")
    print(no2_pivoted, "\n")
    
    # Pivot table with air quality data
    air_pivot_table = air_quality.pivot_table(
        values="value", 
        index="location", 
        columns="parameter", 
        aggfunc="mean"
    )
    print("=== Air quality pivot table (mean concentrations) ===")
    print(air_pivot_table, "\n")
    
    # Wide to long format using melt
    no2_reset = no2.pivot(columns="location", values="value").reset_index()
    print("=== NO2 data in wide format (for melting) ===")
    print(no2_reset.head(), "\n")
    
    no2_melted = no2_reset.melt(id_vars="date.utc")
    print("=== NO2 melted back to long format ===")
    print(no2_melted.head(), "\n")
    
    # More detailed melt with custom names
    no2_melted_detailed = no2_reset.melt(
        id_vars="date.utc",
        value_vars=["BETR801", "FR04014", "London Westminster"],
        value_name="NO_2",
        var_name="id_location"
    )
    print("=== NO2 melted with custom column names ===")
    print(no2_melted_detailed.head(), "\n")

if __name__ == "__main__":
    main()