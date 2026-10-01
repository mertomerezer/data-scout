import pandas as pd

def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df

df = read_csv("data/raw/example.csv")
print(df)

"""Okunan dosya da ki verilerin bilgilerini alma kismi"""
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.isna().sum())
print('Duplicated rows:', df.duplicated().sum())