from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("../models/fraud_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    quantity = float(request.form["Quantity"])
    unit_price = float(request.form["UnitPrice"])

    data = pd.DataFrame({
        "Quantity": [quantity],
        "UnitPrice": [unit_price]
    })

    prediction = model.predict(data)

    if prediction[0] == 1:
        result = "🚨 Fraudulent Return"
    else:
        result = "✅ Safe Return"

    return render_template("index.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)