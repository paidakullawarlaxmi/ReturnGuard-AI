from datetime import datetime

from services.database import get_connection


def save_prediction(database_path, quantity, price, age, previous_returns, prediction, confidence):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with get_connection(database_path) as connection:
        connection.execute(
            """INSERT INTO FraudHistory
            (quantity, price, age, previous_returns, prediction, confidence, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (quantity, price, age, previous_returns, prediction, confidence, timestamp),
        )
    return timestamp


def get_history(database_path, prediction="", min_price=""):
    query, params = "SELECT * FROM FraudHistory WHERE 1=1", []
    if prediction:
        query += " AND prediction LIKE ?"
        params.append(f"%{prediction}%")
    if min_price:
        try:
            query += " AND price >= ?"
            params.append(float(min_price))
        except ValueError:
            pass
    query += " ORDER BY id DESC"
    with get_connection(database_path) as connection:
        return connection.execute(query, params).fetchall()
