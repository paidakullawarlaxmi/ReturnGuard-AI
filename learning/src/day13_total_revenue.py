import pandas as pd

df = pd.read_csv("../data/online_retail.csv")

df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

revenue = df["TotalPrice"].sum()

print("Total Revenue:")
print(revenue)