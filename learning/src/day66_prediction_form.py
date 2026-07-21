from flask import Flask, render_template, request
import joblib

from flask import Flask

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

# Load trained model
model = joblib.load("../models/fraud_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "POST":

        quantity = int(request.form["Quantity"])
        price = float(request.form["UnitPrice"])

        data = [[quantity, price]]

        prediction = model.predict(data)[0]

        if prediction == 1:
            result = "Fraud Return"
        else:
            result = "Genuine Return"

        return render_template("result.html",
                               prediction=result,
                               quantity=quantity,
                               price=price)

    return render_template("predict.html")


if __name__ == "__main__":
    app.run(debug=True)