import pandas as pd

# Load dataset
df = pd.read_csv("../data/online_retail.csv")

print("Dataset Loaded Successfully!")

# Missing values before filling
print("\nMissing Values Before:")
print(df.isnull().sum())

# Fill missing CustomerID with 0
df["CustomerID"] = df["CustomerID"].fillna(0)

# Missing values after filling
print("\nMissing Values After:")
print(df.isnull().sum())