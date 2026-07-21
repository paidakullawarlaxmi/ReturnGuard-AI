import pandas as pd

# Load dataset
df = pd.read_csv("../data/online_retail_featured.csv")

print("Dataset Loaded Successfully!")

print("\nTop 10 Highest Orders")
top10 = df.sort_values(
    by="TotalAmount",
    ascending=False
).head(10)

print(top10)

print("\nTop 10 Lowest Orders")
lowest10 = df.sort_values(
    by="TotalAmount"
).head(10)

print(lowest10)

print("\nSorted by Country and TotalAmount")
print(
    df.sort_values(
        by=["Country", "TotalAmount"]
    ).head(10)
)