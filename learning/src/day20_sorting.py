import pandas as pd

# Load dataset
df = pd.read_csv("../data/online_retail.csv")

# Create TotalPrice column
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Sort highest transactions
sorted_df = df.sort_values("TotalPrice", ascending=False)

print(sorted_df.head(10))