import pandas as pd

df = pd.read_csv("../data/online_retail.csv")

print("Dataset Loaded Successfully!")

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())