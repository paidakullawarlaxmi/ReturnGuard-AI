import pandas as pd

# Load dataset
df = pd.read_csv("../data/online_retail.csv")

print("Dataset Loaded Successfully!")

# Create new column
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

print(df.head())