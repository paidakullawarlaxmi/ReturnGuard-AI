import pandas as pd

# Read dataset
df = pd.read_csv("../data/online_retail.csv")

print("Dataset Loaded Successfully!")

# Count duplicate rows
duplicate_rows = df.duplicated().sum()

print("Duplicate Rows")
print(duplicate_rows)