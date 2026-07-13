import pandas as pd
from sklearn.model_selection import train_test_split

# Load cleaned dataset
df = pd.read_csv("../data/online_retail_cleaned.csv")

print("Dataset Loaded Successfully!")

# Create sample target column
df["Fraud"] = (df["Quantity"] > 20).astype(int)

# Features
X = df[["Quantity", "UnitPrice"]]

# Target
y = df["Fraud"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Feature Shape")
print(X_train.shape)

print("\nTesting Feature Shape")
print(X_test.shape)

print("\nTraining Target Shape")
print(y_train.shape)

print("\nTesting Target Shape")
print(y_test.shape)