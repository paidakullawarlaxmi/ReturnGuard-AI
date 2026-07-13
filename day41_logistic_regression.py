import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("../data/online_retail_cleaned.csv")

print("Dataset Loaded Successfully!")

# Create sample target
df["Fraud"] = (df["Quantity"] > 20).astype(int)

# Features
X = df[["Quantity", "UnitPrice"]]

# Target
y = df["Fraud"]

# Split data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

print("\nModel Trained Successfully!")