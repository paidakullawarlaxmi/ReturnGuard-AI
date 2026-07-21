import pandas as pd

# Load dataset
df = pd.read_csv("../data/online_retail.csv")

# Create TotalPrice column
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Average revenue by country
country_avg = df.groupby("Country")["TotalPrice"].mean()

print(country_avg)