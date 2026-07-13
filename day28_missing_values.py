import pandas as pd

# Load dataset
df = pd.read_csv("../data/online_retail.csv")

print("Dataset Loaded Successfully!")

# Find missing values
missing = df.isnull().sum()

print("\nMissing Values in Each Column:")
print(missing)