from flask import Flask, render_template, request
import pandas as pd
import joblib
import os
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="../static"
)
 
# Load ML model
model_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "fraud_model.pkl"
)

model = joblib.load(model_path)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    quantity = float(request.form["Quantity"])
    unit_price = float(request.form["UnitPrice"])

    sample = pd.DataFrame({
        "Quantity":[quantity],
        "UnitPrice":[unit_price]
    })

    prediction = model.predict(sample)

    if prediction[0] == 1:
        result = "🚨 Fraudulent Return"
    else:
        result = "✅ Genuine Return"

    return render_template(
        "index.html",
        prediction=result
    )


if __name__ == "__main__":
    app.run(debug=True)