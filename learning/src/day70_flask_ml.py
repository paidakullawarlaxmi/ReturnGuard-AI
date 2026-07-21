from flask import Flask, render_template, request
import joblib
import pandas as pd
from datetime import datetime
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)

# Load ML Model
model = joblib.load("../models/fraud_model.pkl")


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


@app.route("/history")
def history():

    file = "../outputs/prediction_history.csv"

    if os.path.exists(file) and os.path.getsize(file) > 0:
        data = pd.read_csv(file)
        records = data.to_dict(orient="records")
    else:
        records = []

    return render_template(
        "history.html",
        records=records
    )


@app.route("/dataset")
def dataset():

    file = "../data/online_retail_cleaned.csv"

    data = pd.read_csv(file)

    records = data.head(100).to_dict(orient="records")

    columns = list(data.columns)

    return render_template(
        "dataset.html",
        records=records,
        columns=columns
    )


@app.route('/dashboard')
def dashboard():
    file = "../outputs/prediction_history.csv"

    if os.path.exists(file) and os.path.getsize(file) > 0:
        data = pd.read_csv(file)
        # prepare counts
        counts = data['Prediction'].value_counts()
        # plot
        plt.figure(figsize=(6,5))
        counts.plot(kind='bar', color=['#2ca02c', '#d62728'])
        plt.title('ReturnGuard AI Prediction Dashboard')
        plt.xlabel('Prediction')
        plt.ylabel('Number of Records')
        out_path = os.path.join('..','static','dashboard.png')
        plt.tight_layout()
        plt.savefig(out_path)
        plt.close()
    else:
        counts = None

    return render_template('dashboard.html', counts=counts)


@app.route("/result", methods=["POST"])
def result():

    quantity = int(request.form["quantity"])
    price = float(request.form["price"])
    age = int(request.form["age"])
    returns = int(request.form["returns"])

    # Features used by model
    features = pd.DataFrame([{
        "Quantity": quantity,
        "UnitPrice": price
    }])

    prediction = model.predict(features)

    probability = model.predict_proba(features)
    confidence = round(max(probability[0]) * 100, 2)

    if prediction[0] == 1:
        fraud = "🚨 HIGH FRAUD"
    else:
        fraud = "✅ LOW FRAUD"

    # Save history
    history_data = pd.DataFrame([{
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Quantity": quantity,
        "Price": price,
        "Age": age,
        "PreviousReturns": returns,
        "Prediction": fraud,
        "Confidence": confidence
    }])

    file = "../outputs/prediction_history.csv"

    if os.path.exists(file):
        history_data.to_csv(file, mode="a", header=False, index=False)
    else:
        history_data.to_csv(file, index=False)

    # Log success
    print("History saved to:", file)
    print(history_data)

    return render_template(
        "result.html",
        prediction=fraud,
        confidence=confidence,
        quantity=quantity,
        price=price,
        age=age,
        returns=returns
    )


if __name__ == "__main__":
    app.run(debug=True)