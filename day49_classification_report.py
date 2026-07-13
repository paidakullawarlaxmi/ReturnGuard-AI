import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("../data/online_retail_cleaned.csv")

print("Dataset Loaded Successfully!")

# Create target column
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

# Train model
model = LogisticRegression()

model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Print Classification Report
print(classification_report(y_test, predictions))