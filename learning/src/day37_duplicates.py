import pandas as pd

# Load dataset
df = pd.read_csv("../data/online_retail_featured.csv")

print("Dataset Loaded Successfully!")

print("\nDataset Shape")
print(df.shape)

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nShowing Duplicate Records")
print(df[df.duplicated()].head())

clean_df = df.drop_duplicates()

print("\nDataset Shape After Removing Duplicates")
print(clean_df.shape)