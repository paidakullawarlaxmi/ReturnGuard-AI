import pandas as pd

# Load dataset
df = pd.read_csv("../data/online_retail_featured.csv")

print("Dataset Loaded Successfully!")

print("\nMissing Values")
print(df.isnull().sum())

print("\nRows After dropna()")
clean_df = df.dropna()
print(clean_df.shape)

print("\nFill Missing CustomerID with -1")
df["CustomerID"] = df["CustomerID"].fillna(-1)

print(df.head())