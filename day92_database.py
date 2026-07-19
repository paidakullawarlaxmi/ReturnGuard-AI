import sqlite3

conn = sqlite3.connect("../database/returnguard.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS FraudHistory(

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

INSERT INTO FraudHistory(

quantity,

price,

age,

previous_returns,

prediction,

confidence

)

VALUES(?,?,?,?,?,?)

""",(25,5.0,12,20,"LOW FRAUD",96))

conn.commit()

cursor.execute("SELECT * FROM FraudHistory")

rows = cursor.fetchall()

print("\n===== FRAUD HISTORY =====\n")

for row in rows:

    print(row)

conn.close()