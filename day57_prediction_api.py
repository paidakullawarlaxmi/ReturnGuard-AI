from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("../models/fraud_model.pkl")

@app.route("/")
def home():
    return "ReturnGuard AI Prediction API"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    quantity = data["Quantity"]
    unit_price = data["UnitPrice"]

    sample = pd.DataFrame({
        "Quantity": [quantity],
        "UnitPrice": [unit_price]
    })

    prediction = model.predict(sample)[0]

    if prediction == 1:
        result = "Fraudulent Return"
    else:
        result = "Genuine Return"

    return jsonify({"Prediction": result})

if __name__ == "__main__":
    app.run(debug=True)