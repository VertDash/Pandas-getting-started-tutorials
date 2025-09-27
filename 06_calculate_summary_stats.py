import pandas as pd

def main():
    url = "https://github.com/pandas-dev/pandas/raw/main/doc/data/titanic.csv"
    titanic = pd.read_csv(url)

    # describe
    print("=== describe() for numeric cols ===")
    print(titanic.describe(), "\n")

    # Group by Sex and Pclass, compute mean Fare
    grouped = titanic.groupby(["Sex", "Pclass"])["Fare"].mean()
    print("=== Mean Fare by Sex and Pclass ===")
    print(grouped, "\n")

    # agg for Age -> mean, median, std
    agg_stats = titanic.groupby("Pclass")["Age"].agg(["count", "mean", "median", "std"])
    print("=== Age statistics per Pclass ===")
    print(agg_stats, "\n")

    # survival rate by Sex and Pclass
    survival = titanic.groupby(["Sex", "Pclass"])["Survived"].mean().unstack()
    print("=== Survival rate (mean) by Sex (rows) and Pclass (columns) ===")
    print(survival)

if __name__ == "__main__":
    main()