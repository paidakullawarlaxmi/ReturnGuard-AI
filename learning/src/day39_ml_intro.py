import pandas as pd

# Load cleaned dataset
df = pd.read_csv("../data/online_retail_cleaned.csv")

print("Dataset Loaded Successfully!")

# Create a sample target column for learning
df["Fraud"] = (df["Quantity"] > 20).astype(int)

# Features
X = df[["Quantity", "UnitPrice"]]

# Target
y = df["Fraud"]

print("\nFeatures")
print(X.head())

print("\nTarget")
print(y.head())