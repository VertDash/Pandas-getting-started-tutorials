import pandas as pd

# Read the air quality data
air_quality = pd.read_csv(
    "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/air_quality_no2_long.csv"
)
print(air_quality.head())

# Check data type of the city column
print(air_quality['city'].dtype)

# Convert location to string and lowercase
air_quality['location'] = air_quality['location'].str.lower()
print(air_quality['location'].head())

# Create new column by extracting the first two characters from location
air_quality['location_code'] = air_quality['location'].str[:2]
print(air_quality[['location', 'location_code']].head())

# Check which locations are in Paris
selector = air_quality['city'].str.contains('Paris')
print(air_quality[selector])

# Split location into parts (if location contains underscore)
if air_quality['location'].str.contains('_').any():
    air_quality[['location_name', 'location_coord']] = air_quality['location'].str.split('_', expand=True)
print(air_quality.head())

# Add column with uppercase city names
air_quality['city_upper'] = air_quality['city'].str.upper()
print(air_quality.head())

# Check if city name contains 'Paris'
print(air_quality['city'].str.contains('Paris'))

# Create series of pandas strings
s = pd.Series(['A', 'B', 'C', 'AaBb', 'BaCa'])
print(s.str.lower())  # Convert to lowercase
print(s.str.upper())  # Convert to uppercase
print(s.str.len())    # Length of each string

# Chain string methods
print(air_quality['location'].value_counts())