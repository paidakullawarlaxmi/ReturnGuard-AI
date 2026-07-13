import pandas as pd

# Load processed dataset
df = pd.read_csv("../data/online_retail_featured.csv")

print("Dataset Loaded Successfully!")

print("\nOrders above 1000")
high_orders = df[df["TotalAmount"] > 1000]
print(high_orders.head())

print("\nUnited Kingdom Orders")
uk_orders = df[df["Country"] == "United Kingdom"]
print(uk_orders.head())

print("\nOrders above 5000 using loc")
print(df.loc[df["TotalAmount"] > 5000].head())

print("\nUK Orders Above 1000")
result = df[
    (df["Country"] == "United Kingdom")
    &
    (df["TotalAmount"] > 1000)
]
print(result.head())