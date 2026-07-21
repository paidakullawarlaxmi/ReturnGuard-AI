from datetime import datetime

from flask import Blueprint, current_app, redirect, render_template, request, send_file, session, url_for

from services.chart_service import generate_fraud_chart
from services.database import get_connection, log_activity
from services.fraud_service import assess_return, impact_weights
from services.history_service import get_history, save_prediction
from services.report_service import generate_reports

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    return render_template("home.html")


@main_bp.route("/predict")
def predict():
    return render_template("predict.html")


@main_bp.route("/result", methods=["POST"])
def result():
    try:
        quantity, price = int(request.form["quantity"]), float(request.form["price"])
        age, previous_returns = int(request.form["age"]), int(request.form["returns"])
    except (KeyError, TypeError, ValueError):
        return redirect(url_for("main.predict"))
    outcome = assess_return(current_app.extensions["fraud_model"], quantity, price, age, previous_returns)
    timestamp = save_prediction(current_app.config["DATABASE_PATH"], quantity, price, age, previous_returns, outcome.prediction, outcome.confidence)
    weights = impact_weights(quantity, price, age, previous_returns)
    recommendation = "Approve Return" if outcome.prediction == "LOW FRAUD" else "Investigate Before Approval"
    details = {"prediction": outcome.prediction, "confidence": f"{outcome.confidence}%", "recommendation": recommendation, "timestamp": timestamp, "investigator": session.get("username", "System"), "quantity": quantity, "unit_price": f"${price:.2f}", "customer_age": age, "previous_returns": previous_returns}
    generate_reports(current_app.config["PDF_REPORT_PATH"], current_app.config["EMAIL_REPORT_PATH"], details)
    log_activity(current_app.config["DATABASE_PATH"], f"Prediction generated: {outcome.prediction}", session.get("username", "System"))
    return render_template("result.html", prediction=outcome.prediction, confidence=outcome.confidence, recommendation=recommendation, quantity=quantity, price=price, age=age, returns=previous_returns, shap_vals=weights)


@main_bp.route("/dashboard")
def dashboard():
    generate_fraud_chart(current_app.config["DATABASE_PATH"], current_app.config["CHART_PATH"])
    with get_connection(current_app.config["DATABASE_PATH"]) as connection:
        total = connection.execute("SELECT COUNT(*) FROM FraudHistory").fetchone()[0]
        high = connection.execute("SELECT COUNT(*) FROM FraudHistory WHERE prediction LIKE '%HIGH%'").fetchone()[0]
        low = connection.execute("SELECT COUNT(*) FROM FraudHistory WHERE prediction LIKE '%LOW%'").fetchone()[0]
        users = connection.execute("SELECT COUNT(*) FROM Users").fetchone()[0]
        logs = connection.execute("SELECT * FROM ActivityLog ORDER BY id DESC LIMIT 15").fetchall()
    return render_template("dashboard.html", stats={"total_scans": total, "high_fraud": high, "low_fraud": low, "active_users": users, "has_chart": current_app.config["CHART_PATH"].exists(), "timestamp": int(datetime.now().timestamp())}, logs=logs)


@main_bp.route("/history")
def history():
    prediction, min_price = request.args.get("prediction", ""), request.args.get("min_price", "")
    return render_template("history.html", records=get_history(current_app.config["DATABASE_PATH"], prediction, min_price), req_prediction=prediction, req_min_price=min_price)


@main_bp.route("/reports")
def reports():
    path = current_app.config["EMAIL_REPORT_PATH"]
    content = path.read_text(encoding="utf-8") if path.exists() else "Submit a prediction first to generate a report."
    return render_template("reports.html", email_content=content)


@main_bp.route("/reports/pdf")
def download_pdf():
    path = current_app.config["PDF_REPORT_PATH"]
    return send_file(path, as_attachment=True) if path.exists() else ("Report not generated.", 404)


@main_bp.route("/reports/email")
def download_email():
    path = current_app.config["EMAIL_REPORT_PATH"]
    return send_file(path, as_attachment=True, download_name="fraud_email.txt") if path.exists() else ("Email draft not generated.", 404)
