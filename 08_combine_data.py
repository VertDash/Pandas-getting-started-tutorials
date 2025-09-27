import pandas as pd

def main():
    # Load the three datasets used in the tutorial
    
    # 1. Air quality NO2 data
    air_quality_no2_url = "https://github.com/pandas-dev/pandas/raw/main/doc/data/air_quality_no2_long.csv"
    air_quality_no2 = pd.read_csv(air_quality_no2_url, parse_dates=True)
    air_quality_no2 = air_quality_no2[["date.utc", "location", "parameter", "value"]]
    
    # 2. Air quality PM2.5 data  
    air_quality_pm25_url = "https://github.com/pandas-dev/pandas/raw/main/doc/data/air_quality_pm25_long.csv"
    air_quality_pm25 = pd.read_csv(air_quality_pm25_url, parse_dates=True)
    air_quality_pm25 = air_quality_pm25[["date.utc", "location", "parameter", "value"]]
    
    # 3. Stations coordinates metadata
    stations_url = "https://github.com/pandas-dev/pandas/raw/main/doc/data/air_quality_stations.csv"
    stations_coord = pd.read_csv(stations_url)
    
    # 4. Parameters metadata
    parameters_url = "https://github.com/pandas-dev/pandas/raw/main/doc/data/air_quality_parameters.csv" 
    air_quality_parameters = pd.read_csv(parameters_url)
    
    print("=== ORIGINAL DATASETS ===")
    print("NO2 data shape:", air_quality_no2.shape)
    print(air_quality_no2.head(), "\n")
    
    print("PM2.5 data shape:", air_quality_pm25.shape)
    print(air_quality_pm25.head(), "\n")
    
    print("Stations coordinates:")
    print(stations_coord.head(), "\n")
    
    print("Parameters metadata:")
    print(air_quality_parameters.head(), "\n")
    
    # === CONCATENATING DATAFRAMES ===
    print("=== CONCATENATING DATAFRAMES ===")
    
    # Combine NO2 and PM2.5 data (row-wise concatenation)
    air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
    
    print("After concatenation:")
    print(f"PM2.5 table shape: {air_quality_pm25.shape}")
    print(f"NO2 table shape: {air_quality_no2.shape}")
    print(f"Combined table shape: {air_quality.shape}")
    print(f"Total rows: {air_quality_pm25.shape[0]} + {air_quality_no2.shape[0]} = {air_quality.shape[0]}")
    print()
    
    # Sort by date to see the combination
    air_quality = air_quality.sort_values("date.utc")
    print("Combined data (sorted by date):")
    print(air_quality.head(), "\n")
    
    # Concatenation with keys (hierarchical index)
    print("=== CONCATENATION WITH KEYS ===")
    air_quality_keyed = pd.concat([air_quality_pm25, air_quality_no2], keys=["PM25", "NO2"])
    print("Concatenation with hierarchical index:")
    print(air_quality_keyed.head(), "\n")
    
    # Reset index to convert hierarchical index to column
    print("Reset index to make hierarchical index a column:")
    air_quality_reset = air_quality_keyed.reset_index(level=0)
    print(air_quality_reset.head(), "\n")
    
    # === JOINING TABLES USING MERGE ===
    print("=== JOINING TABLES WITH MERGE ===")
    
    # Merge with station coordinates
    print("Before merge - air_quality columns:", list(air_quality.columns))
    print("Stations data:")
    print(stations_coord[stations_coord['location'].isin(['FR04014', 'BETR801', 'London Westminster'])], "\n")
    
    air_quality_with_coords = pd.merge(air_quality, stations_coord, how="left", on="location")
    print("After merging with station coordinates:")
    print(f"Shape: {air_quality_with_coords.shape}")
    print("Columns:", list(air_quality_with_coords.columns))
    print(air_quality_with_coords.head(), "\n")
    
    # Merge with parameter descriptions (different column names)
    print("=== MERGE WITH DIFFERENT COLUMN NAMES ===")
    print("Parameters metadata:")
    print(air_quality_parameters, "\n")
    
    air_quality_final = pd.merge(
        air_quality_with_coords, 
        air_quality_parameters,
        how='left', 
        left_on='parameter',  # column in left table
        right_on='id'         # column in right table
    )
    
    print("After merging with parameter descriptions:")
    print(f"Final shape: {air_quality_final.shape}")
    print("Final columns:", list(air_quality_final.columns))
    print(air_quality_final.head(), "\n")
    
    # === DIFFERENT TYPES OF JOINS ===
    print("=== DIFFERENT JOIN TYPES ===")
    
    # Create small sample data to demonstrate different joins
    left_df = pd.DataFrame({
        'key': ['A', 'B', 'C', 'D'],
        'left_val': [1, 2, 3, 4]
    })
    
    right_df = pd.DataFrame({
        'key': ['B', 'C', 'D', 'E'], 
        'right_val': [5, 6, 7, 8]
    })
    
    print("Left DataFrame:")
    print(left_df, "\n")
    print("Right DataFrame:")
    print(right_df, "\n")
    
    # Inner join (default)
    inner_join = pd.merge(left_df, right_df, on='key', how='inner')
    print("Inner join (only matching keys):")
    print(inner_join, "\n")
    
    # Left join
    left_join = pd.merge(left_df, right_df, on='key', how='left')
    print("Left join (all from left table):")
    print(left_join, "\n")
    
    # Right join
    right_join = pd.merge(left_df, right_df, on='key', how='right')
    print("Right join (all from right table):")
    print(right_join, "\n")
    
    # Outer join
    outer_join = pd.merge(left_df, right_df, on='key', how='outer')
    print("Outer join (all records from both tables):")
    print(outer_join, "\n")
    
    # === COLUMN-WISE CONCATENATION ===
    print("=== COLUMN-WISE CONCATENATION ===")
    
    # Create sample data for column-wise concatenation
    df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df2 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
    
    print("DataFrame 1:")
    print(df1, "\n")
    print("DataFrame 2:")
    print(df2, "\n")
    
    # Concatenate along columns (axis=1)
    col_concat = pd.concat([df1, df2], axis=1)
    print("Column-wise concatenation (axis=1):")
    print(col_concat, "\n")
    
    print("=== SUMMARY ===")
    print("Key operations demonstrated:")
    print("1. pd.concat() - combines tables row-wise (axis=0) or column-wise (axis=1)")
    print("2. pd.merge() - database-style joins using common keys")
    print("3. Join types: inner, left, right, outer")
    print("4. Different column names: use left_on and right_on parameters")
    print("5. Keys parameter in concat() creates hierarchical index")

if __name__ == "__main__":
    main()