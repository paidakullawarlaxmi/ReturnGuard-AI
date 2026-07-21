# ReturnGuard AI

AI-powered return-fraud detection system built with Flask and scikit-learn. It evaluates return requests, stores an audit history, presents dashboard analytics, and produces investigation reports.

## Features

- Fraud prediction with a saved ML model and a safe fallback rule
- Login and signup flow with SQLite persistence
- Prediction history, filters, activity log, and analytics dashboard
- PDF and email-style investigation reports
- Modular Flask routes, services, and machine-learning code

## Project structure

```text
ReturnGuard-AI/
├── app.py                 # Application entry point
├── config/                # Runtime paths and configuration
├── data/                  # Source datasets
├── database/              # Local SQLite database (generated)
├── learning/              # Day-wise practice work, kept separate
├── models/                # Trained ML artifacts
├── routes/                # Flask blueprints
├── services/              # Database, reports, fraud, and chart logic
├── src/                   # ML feature and prediction modules
├── static/css/            # Front-end styles
├── templates/             # HTML views
├── tests/                 # Automated tests
├── logs/                  # Runtime logs (generated)
└── reports/               # Generated reports
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`. For a fresh database, the starter administrator is `admin` / `admin`; change this before any real deployment.

## Tech stack

Python, Flask, Pandas, NumPy, scikit-learn, SQLite, Matplotlib, ReportLab, HTML, and CSS.

## Testing

```bash
pytest
```
