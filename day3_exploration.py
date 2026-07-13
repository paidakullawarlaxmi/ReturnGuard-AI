import pandas as pd

# Load dataset
df = pd.read_csv("../data/online_retail.csv")

print("Dataset Loaded Successfully!")

print("\nNumber of Rows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())