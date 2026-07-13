import pandas as pd

# Load Dataset
df = pd.read_csv("../data/online_retail.csv")

print("Dataset Loaded Successfully!")

print("\nUnited Kingdom Transactions")

uk_data = df[df["Country"] == "United Kingdom"]

print(uk_data.head())