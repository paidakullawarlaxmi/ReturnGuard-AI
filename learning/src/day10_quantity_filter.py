import pandas as pd

# Load Dataset
df = pd.read_csv("../data/online_retail.csv")

print("Dataset Loaded Successfully!")

high_quantity = df[df["Quantity"] > 100]

print("\nOrders with Quantity Greater Than 100")

print(high_quantity.head())