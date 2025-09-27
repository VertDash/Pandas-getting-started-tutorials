import pandas as pd

def main():
    url = "https://github.com/pandas-dev/pandas/raw/main/doc/data/titanic.csv"
    titanic = pd.read_csv(url)

    # Select a single column and multiple columns
    ages = titanic["Age"]                 # Series
    age_sex = titanic[["Age", "Sex"]]     # DataFrame
    print("=== ages (Series) head ===")
    print(ages.head(), "\n")
    print("=== age & sex (DataFrame) head ===")
    print(age_sex.head(), "\n")

    # Filtering rows (boolean)
    above_35 = titanic[titanic["Age"] > 35]
    print("=== Age > 35 sample ===")
    print(above_35.head(), "\n")

    # .isin example
    pclass_23 = titanic[titanic["Pclass"].isin([2, 3])]
    print("=== Pclass in [2,3] sample ===")
    print(pclass_23.head(), "\n")

    # .notna()
    has_age = titanic[titanic["Age"].notna()]
    print("Number with non-missing Age:", has_age.shape[0], "\n")

    # .loc and .iloc
    children = titanic.loc[titanic["Age"] < 18, ["Name", "Sex", "Age"]]
    print("=== Children (Name, Sex, Age) ===")
    print(children.head(), "\n")

    first_rows_slice = titanic.iloc[0:3, 0:5]
    print("=== iloc first 3 rows, first 5 cols ===")
    print(first_rows_slice)

    # safe assignment with .loc for setting
    titanic_copy = titanic.copy()
    cond = titanic_copy["Age"] < 10
    titanic_copy.loc[cond, "Name"] = "Child - anonymized"
    print("\nExample of assignment via .loc (first 5 changes):")
    print(titanic_copy.loc[cond, ["Name", "Age"]].head())

if __name__ == "__main__":
    main()