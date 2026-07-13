from flask import Flask, render_template, request

app = Flask(__name__)

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

    score = 0

    if quantity > 5:
        score += 20

    if price > 1000:
        score += 30

    if returns >= 3:
        score += 40

    if age < 20:
        score += 10

    if score >= 60:
        prediction = "HIGH FRAUD"
    elif score >= 30:
        prediction = "MEDIUM FRAUD"
    else:
        prediction = "LOW FRAUD"

    return render_template(
        "result.html",
        prediction=prediction,
        score=score,
        quantity=quantity,
        price=price,
        age=age,
        returns=returns
    )


if __name__ == "__main__":
    app.run(debug=True)