import sqlite3

connection = sqlite3.connect("../database/fraud.db")

cursor = connection.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS fraud_predictions(

id INTEGER PRIMARY KEY AUTOINCREMENT,

quantity INTEGER,

price REAL,

age INTEGER,

previous_returns INTEGER,

prediction TEXT,

confidence REAL

)

""")

cursor.execute("""

INSERT INTO fraud_predictions(

quantity,

price,

age,

previous_returns,

prediction,

confidence

)

VALUES(?,?,?,?,?,?)

""",(25,5,12,20,"LOW FRAUD",96))

connection.commit()

cursor.execute("SELECT * FROM fraud_predictions")

rows = cursor.fetchall()

print("Fraud Prediction History")

for row in rows:
    print(row)

connection.close()