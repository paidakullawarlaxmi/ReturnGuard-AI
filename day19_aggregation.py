import pandas as pd

# Load dataset
df = pd.read_csv("../data/online_retail.csv")

# Create TotalPrice column
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Aggregation by country
country_stats = df.groupby("Country")["TotalPrice"].agg(
    ["sum", "mean", "max", "min", "count"]
)

print(country_stats)