import pandas as pd

# Load dataset
df = pd.read_csv("../data/online_retail.csv")

# Create TotalPrice
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Calculate mean (average)
avg_value = df["TotalPrice"].mean()

print("Average Transaction Value:", avg_value)