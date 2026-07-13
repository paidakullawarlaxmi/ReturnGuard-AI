import pandas as pd

# Load dataset
df = pd.read_csv("../data/online_retail.csv")

# Create TotalPrice column
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Minimum value
min_value = df["TotalPrice"].min()

# Maximum value
max_value = df["TotalPrice"].max()

print("Minimum Transaction Value:", min_value)
print("Maximum Transaction Value:", max_value)