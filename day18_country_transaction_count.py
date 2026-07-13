import pandas as pd

# Load dataset
df = pd.read_csv("../data/online_retail.csv")

# Create TotalPrice column
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Count transactions by country
country_count = df.groupby("Country")["TotalPrice"].count()

print(country_count)