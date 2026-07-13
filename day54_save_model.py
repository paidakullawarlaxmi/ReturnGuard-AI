import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("../data/online_retail_cleaned.csv")

print("Dataset Loaded Successfully!")

# Create target column
df["Fraud"] = (df["Quantity"] > 20).astype(int)

# Features
X = df[["Quantity", "UnitPrice"]]

# Target
y = df["Fraud"]

# Train model
model = LogisticRegression(max_iter=1000)

model.fit(X, y)

print("Model Trained Successfully!")

# Save model
joblib.dump(model, "../models/fraud_model.pkl")

print("Model Saved Successfully!")