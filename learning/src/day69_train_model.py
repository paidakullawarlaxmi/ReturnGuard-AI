
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# ----------------------------
# Load Dataset
# ----------------------------
data = pd.read_csv("../data/online_retail_cleaned.csv")

# ----------------------------
# Create Fraud Label
# ----------------------------
data["Fraud"] = (
    (data["Quantity"] > 5)
    &
    (data["UnitPrice"] > 1000)
).astype(int)

# ----------------------------
# Features
# ----------------------------
X = data[[
    "Quantity",
    "UnitPrice"
]]

# ----------------------------
# Target
# ----------------------------
y = data["Fraud"]

# ----------------------------
# Train Test Split
# ----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ----------------------------
# Train Model
# ----------------------------
model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

# ----------------------------
# Prediction
# ----------------------------
prediction = model.predict(X_test)

# ----------------------------
# Accuracy
# ----------------------------
accuracy = accuracy_score(y_test, prediction)

print("Accuracy :", accuracy)

# ----------------------------
# Save Model
# ----------------------------
joblib.dump(model, "../models/fraud_model.pkl")

print("Model Saved Successfully")