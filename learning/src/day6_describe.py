import pandas as pd

# Load Dataset
df = pd.read_csv("../data/online_retail.csv")

print("Dataset Loaded Successfully!")

print("\nStatistics Summary")

print(df.describe())