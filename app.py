"""ReturnGuard AI application entry point."""
import logging
from pathlib import Path

from flask import Flask, redirect, request, session, url_for

from config.config import Config
from routes.auth import auth_bp
from routes.main import main_bp
from services.database import initialize_database
from services.fraud_service import load_model


def create_app(test_config=None):
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(Config)
    if test_config:
        app.config.update(test_config)
    for directory in (app.config["DATABASE_PATH"].parent, app.config["REPORTS_DIR"], app.config["LOGS_DIR"], app.config["CHART_PATH"].parent):
        Path(directory).mkdir(parents=True, exist_ok=True)
    logging.basicConfig(filename=app.config["LOGS_DIR"] / "app.log", level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    initialize_database(app.config["DATABASE_PATH"])
    app.extensions["fraud_model"] = load_model(app.config["MODEL_PATH"])

    @app.before_request
    def require_login():
        if request.endpoint and request.endpoint not in {"auth.login", "auth.signup", "static"} and "username" not in session:
            return redirect(url_for("auth.login"))

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)

