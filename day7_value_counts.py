import pandas as pd

# Load dataset
df = pd.read_csv("../data/online_retail.csv")

print("Dataset Loaded Successfully!")

print("\nOrders By Country")

print(df["Country"].value_counts())