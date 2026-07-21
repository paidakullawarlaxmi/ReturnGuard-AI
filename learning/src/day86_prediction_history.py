import csv
import os
from datetime import datetime

prediction = "LOW FRAUD"
confidence = 96

quantity = 25
price = 5
age = 12
previous_returns = 20

file_name = "../outputs/prediction_history.csv"

file_exists = os.path.exists(file_name)

with open(file_name, "a", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    if not file_exists:
        writer.writerow([
            "Date",
            "Prediction",
            "Confidence",
            "Quantity",
            "Price",
            "Age",
            "PreviousReturns"
        ])

    writer.writerow([
        datetime.now(),
        prediction,
        confidence,
        quantity,
        price,
        age,
        previous_returns
    ])

print("Prediction saved successfully!")