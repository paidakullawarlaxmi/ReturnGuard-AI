import pandas as pd

# Read dataset
df = pd.read_csv("../data/online_retail_featured.csv")

print("Dataset Loaded Successfully!")

# Remove missing values
df = df.dropna()

# Remove duplicate rows
df = df.drop_duplicates()

print("Clean Dataset Shape")
print(df.shape)

# Save cleaned dataset
df.to_csv(
    "../data/online_retail_cleaned.csv",
    index=False
)

print("Dataset Saved Successfully!")