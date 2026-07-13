import pandas as pd

df = pd.read_csv("../data/online_retail.csv")

print("Dataset Loaded Successfully!")

print(df.shape)
print(df.head())
print(df.columns)