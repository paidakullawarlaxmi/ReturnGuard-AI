import sqlite3
from datetime import datetime

from werkzeug.security import generate_password_hash


def get_connection(database_path):
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database(database_path):
    with get_connection(database_path) as connection:
        connection.executescript("""
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL DEFAULT 'user'
            );
            CREATE TABLE IF NOT EXISTS FraudHistory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL,
                age INTEGER NOT NULL,
                previous_returns INTEGER NOT NULL,
                prediction TEXT NOT NULL,
                confidence REAL NOT NULL,
                timestamp TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS ActivityLog (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                activity TEXT NOT NULL,
                time TEXT NOT NULL,
                username TEXT NOT NULL
            );
        """)
        if connection.execute("SELECT COUNT(*) FROM Users").fetchone()[0] == 0:
            connection.execute(
                "INSERT INTO Users (username, password, role) VALUES (?, ?, ?)",
                ("admin", generate_password_hash("admin"), "admin"),
            )


def log_activity(database_path, activity, username="System"):
    with get_connection(database_path) as connection:
        connection.execute(
            "INSERT INTO ActivityLog (activity, time, username) VALUES (?, ?, ?)",
            (activity, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), username),
        )
