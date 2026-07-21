from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("../models/fraud_model.pkl","rb"))


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/predict")
def predict():
    return render_template("predict.html")


@app.route("/result", methods=["POST"])
def result():

    quantity = int(request.form["quantity"])
    price = float(request.form["price"])
    age = int(request.form["age"])
    returns = int(request.form["returns"])

    features = pd.DataFrame({
        "Quantity":[quantity],
        "UnitPrice":[price],
        "CustomerAge":[age],
        "PreviousReturns":[returns]
    })

    prediction = model.predict(features)

    if prediction[0] == 1:
        fraud = "🚨 HIGH FRAUD"
    else:
        fraud = "✅ LOW FRAUD"

    return render_template(
        "result.html",
        prediction=fraud,
        quantity=quantity,
        price=price,
        age=age,
        returns=returns
    )


if __name__ == "__main__":
    app.run(debug=True)