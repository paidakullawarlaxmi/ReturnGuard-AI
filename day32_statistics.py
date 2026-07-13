import pandas as pd

# Load featured dataset
df = pd.read_csv("../data/online_retail_featured.csv")

print("Dataset Loaded Successfully!")

print("\nLast 5 Rows")
print(df.tail())

print("\nStatistics")
print(df.describe())

print("\nAverage Total Amount")
print(df["TotalAmount"].mean())

print("\nHighest Total Amount")
print(df["TotalAmount"].max())

print("\nLowest Total Amount")
print(df["TotalAmount"].min())

print("\nTotal Orders")
print(df["TotalAmount"].count())

print("\nUnique Countries")
print(df["Country"].nunique())