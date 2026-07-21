import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


class Config:
    SECRET_KEY = os.environ.get("RETURNGUARD_SECRET_KEY", "change-this-development-key")
    DATABASE_PATH = BASE_DIR / "database" / "returnguard.db"
    MODEL_PATH = BASE_DIR / "models" / "fraud_model.pkl"
    REPORTS_DIR = BASE_DIR / "reports"
    LOGS_DIR = BASE_DIR / "logs"
    CHART_PATH = BASE_DIR / "static" / "images" / "fraud_bar.png"
    PDF_REPORT_PATH = REPORTS_DIR / "fraud_report.pdf"
    EMAIL_REPORT_PATH = REPORTS_DIR / "fraud_email.txt"
