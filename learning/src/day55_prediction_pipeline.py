import joblib

# -----------------------------
# Step 1: Load Saved Model
# -----------------------------
model = joblib.load("../models/fraud_model.pkl")

print("Model Loaded Successfully!")

# -----------------------------
# Step 2: Get User Input
# -----------------------------
quantity = float(input("Enter Quantity: "))
unit_price = float(input("Enter Unit Price: "))

# -----------------------------
# Step 3: Create Input Data
# -----------------------------
new_data = [[quantity, unit_price]]

# -----------------------------
# Step 4: Make Prediction
# -----------------------------
prediction = model.predict(new_data)

# -----------------------------
# Step 5: Show Result
# -----------------------------
if prediction[0] == 1:
    print("🚨 Fraudulent Return Detected")
else:
    print("✅ Genuine Return")