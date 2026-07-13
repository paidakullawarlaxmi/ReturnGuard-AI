import pandas as pd

# Load dataset
df = pd.read_csv("../data/online_retail.csv")

# Create TotalPrice column
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Minimum order value by country
country_min = df.groupby("Country")["TotalPrice"].min()

print(country_min)