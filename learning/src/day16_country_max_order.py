import pandas as pd

# Load dataset
df = pd.read_csv("../data/online_retail.csv")

# Create TotalPrice column
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Highest order value per country
country_max = df.groupby("Country")["TotalPrice"].max()

print(country_max)