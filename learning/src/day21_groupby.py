import pandas as pd

# Load dataset
df = pd.read_csv("../data/online_retail.csv")

# Create TotalPrice column
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Group by Country and sum
result = df.groupby("Country")["TotalPrice"].sum()

print(result)