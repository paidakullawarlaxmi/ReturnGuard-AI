import pandas as pd

# Load dataset
df = pd.read_csv("../data/online_retail.csv")

print("Dataset Loaded Successfully!")

# Highest Unit Price
highest_price = df["UnitPrice"].max()

# Lowest Unit Price
lowest_price = df["UnitPrice"].min()

print("\nHighest Unit Price:")
print(highest_price)

print("\nLowest Unit Price:")
print(lowest_price)