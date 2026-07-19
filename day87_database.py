import sqlite3

connection = sqlite3.connect("../fraud_history.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS fraud_history(

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

INSERT INTO fraud_history(

quantity,
price,
age,
previous_returns,
prediction,
confidence

)

VALUES(?,?,?,?,?,?)

""",(25,5.0,12,20,"LOW FRAUD",96))

connection.commit()

cursor.execute("SELECT * FROM fraud_history")

rows = cursor.fetchall()

print("\nFraud History\n")

for row in rows:
    print(row)

connection.close()