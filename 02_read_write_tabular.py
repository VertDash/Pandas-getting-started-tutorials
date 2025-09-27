import pandas as pd
import os

def main():
    # grab titanic data straight from pandas github url
    url = "https://github.com/pandas-dev/pandas/raw/main/doc/data/titanic.csv"
    titanic = pd.read_csv(url)
    print("=== Titanic head ===")
    print(titanic.head(), "\n")

    # quick check
    print("Columns:", list(titanic.columns))
    print("Dtypes:\n", titanic.dtypes, "\n")

    # save a sample to see how it looks
    out_dir = "examples_output"
    os.makedirs(out_dir, exist_ok=True)

    sample = titanic.head(10)
    csv_path = os.path.join(out_dir, "titanic_head.csv")
    json_path = os.path.join(out_dir, "titanic_head.json")
    sample.to_csv(csv_path, index=False)
    sample.to_json(json_path, orient="records", lines=False)
    print(f"Wrote sample to {csv_path} and {json_path}\n")

    # Read them back to confirm its the same
    re_csv = pd.read_csv(csv_path)
    print("Re-read CSV shape:", re_csv.shape)

if __name__ == "__main__":
    main()
