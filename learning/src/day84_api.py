from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "ReturnGuard AI API"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    quantity = data["Quantity"]
    price = data["Price"]
    age = data["Age"]
    previous = data["PreviousReturns"]

    if previous > 10:
        prediction = "HIGH FRAUD"
        confidence = 96
    else:
        prediction = "LOW FRAUD"
        confidence = 90

    return jsonify({
        "Prediction": prediction,
        "Confidence": confidence
    })

if __name__ == "__main__":
    app.run(debug=True)