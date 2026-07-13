import pandas as pd

# Load dataset
df = pd.read_csv("../data/online_retail.csv")

print("Dataset Loaded Successfully!")

result = df[
    (df["Country"] == "France") &
    (df["Quantity"] > 50)
]

print(result.head())