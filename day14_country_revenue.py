import pandas as pd

# Load dataset
df = pd.read_csv("../data/online_retail.csv")

# Create TotalPrice column
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Country wise revenue
country_revenue = df.groupby("Country")["TotalPrice"].sum()

print(country_revenue)
