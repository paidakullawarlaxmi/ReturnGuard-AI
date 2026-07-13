import pandas as pd

# Read featured dataset
df = pd.read_csv("../data/online_retail_featured.csv")

print("Dataset Loaded Successfully!")

print("\nTotal Sales by Country")

country_sales = df.groupby("Country")["TotalAmount"].sum()

country_sales = country_sales.sort_values(ascending=False)

print(country_sales)

print("\nAverage Sales by Country")

print(df.groupby("Country")["TotalAmount"].mean())

print("\nNumber of Orders by Country")

print(df.groupby("Country")["InvoiceNo"].count())