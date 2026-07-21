from flask import Blueprint, current_app, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from services.database import get_connection, log_activity

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username, password = request.form.get("username", "").strip(), request.form.get("password", "")
        with get_connection(current_app.config["DATABASE_PATH"]) as connection:
            user = connection.execute("SELECT * FROM Users WHERE username=?", (username,)).fetchone()
        if user and check_password_hash(user["password"], password):
            session.update(username=user["username"], role=user["role"])
            log_activity(current_app.config["DATABASE_PATH"], "User logged in", user["username"])
            return redirect(url_for("main.home"))
        return render_template("login.html", error="Invalid username or password")
    return render_template("login.html")


@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username, password = request.form.get("username", "").strip(), request.form.get("password", "")
        if not username or not password:
            return render_template("signup.html", error="Please fill in all fields")
        try:
            with get_connection(current_app.config["DATABASE_PATH"]) as connection:
                connection.execute("INSERT INTO Users (username, password, role) VALUES (?, ?, ?)", (username, generate_password_hash(password), "user"))
        except Exception:
            return render_template("signup.html", error="Username already exists")
        log_activity(current_app.config["DATABASE_PATH"], "User registered", username)
        return render_template("login.html", msg="Registration successful. Please log in.")
    return render_template("signup.html")


@auth_bp.route("/logout")
def logout():
    log_activity(current_app.config["DATABASE_PATH"], "User logged out", session.get("username", "System"))
    session.clear()
    return redirect(url_for("auth.login"))
