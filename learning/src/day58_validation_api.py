from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("../models/fraud_model.pkl")

@app.route("/")
def home():
    return "ReturnGuard AI Validation API Running!"

@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json()

        if "Quantity" not in data:
            return jsonify({"Error": "Quantity is missing"}), 400

        if "UnitPrice" not in data:
            return jsonify({"Error": "UnitPrice is missing"}), 400

        quantity = data["Quantity"]
        price = data["UnitPrice"]

        sample = pd.DataFrame({
            "Quantity": [quantity],
            "UnitPrice": [price]
        })

        prediction = model.predict(sample)

        if prediction[0] == 1:
            result = "Fraudulent Return"
        else:
            result = "Genuine Return"

        return jsonify({
            "Prediction": result
        })

    except Exception as e:

        return jsonify({
            "Error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)