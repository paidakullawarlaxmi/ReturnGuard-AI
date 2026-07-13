from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Create Flask app
app = Flask(__name__)

# Load trained model
model = joblib.load("../models/fraud_model.pkl")

@app.route("/")
def home():
    return "ReturnGuard AI API is Running!"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    quantity = data["Quantity"]
    unit_price = data["UnitPrice"]

    input_df = pd.DataFrame({
        "Quantity": [quantity],
        "UnitPrice": [unit_price]
    })

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        result = "Fraudulent Return"
    else:
        result = "Genuine Return"

    return jsonify({
        "Prediction": result
    })

if __name__ == "__main__":
    app.run(debug=True)