import pandas as pd

# Step 1: Read the original dataset
df = pd.read_csv("../data/online_retail.csv")

print("Dataset Loaded Successfully!")

# Step 2: Create a new column
df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

print("New Column Created Successfully!")

# Step 3: Show first 5 rows
print(df.head())

# Step 4: Save the new dataset
df.to_csv("../data/online_retail_featured.csv", index=False)

print("New Dataset Saved Successfully!")