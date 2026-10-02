import pandas as pd

def read_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: CSV file not found: {file_path}")
        return None

df = read_csv(input("Enter the path to the CSV file: "))

if df is not None:
    print("\n=== DATASET OVERVIEW ===")
    print(df)
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print("\nColumn names:")
    print(df.columns.tolist())
    print("\nData types:")
    print(df.dtypes)

    print("\n=== DATA QUALITY ===")
    print("\nMissing values per column:")
    print(df.isna().sum())
    print('Duplicated rows:', df.duplicated().sum())
    print(df.columns[df.isna().all()])

    print("\n=== COLUMN DETAILS ===")
    print("\nUnique values per column:")
    print(df.nunique())
    print("\nNumeric columns:")
    print(df.select_dtypes(include=["number"]).columns)
    print("\nText columns:")
    print(df.select_dtypes(include=["object","string"]).columns)

    print("\n=== STATISTICAL SUMMARY ===")
    print(df.describe(include="all"))
