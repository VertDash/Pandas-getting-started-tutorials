import pandas as pd

def main():
    # 1. Create DataFrame from a dictionary
    data = {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
    df = pd.DataFrame(data)
    print("DataFrame:")
    print(df)
    print("\n")

    # 2. Access a single column → Series
    ages_series = df["Age"]
    print("Series (Age column):")
    print(ages_series)
    print("\n")

    # 3. Make a Series
    ages2 = pd.Series([22, 35, 58], name="Age2")
    print("Standalone Series ages2:")
    print(ages2)
    print("\n")

    # 4. Basic stats
    print("Max age via DataFrame selection:", df["Age"].max())
    print("Max via explicit Series object:", ages2.max())
    print("\n")

    
    print("Descriptive statistics of df:")
    print(df.describe())

if __name__ == "__main__":
    main()