import sqlite3
from datetime import datetime

conn = sqlite3.connect("../database/returnguard.db")

cursor = conn.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS ActivityLog(

id INTEGER PRIMARY KEY AUTOINCREMENT,

activity TEXT,

time TEXT

)

""")

def log_activity(activity):

    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    cursor.execute(

        "INSERT INTO ActivityLog(activity,time) VALUES(?,?)",

        (activity,current_time)

    )

    conn.commit()

log_activity("Website Opened")

log_activity("Fraud Prediction Generated")

log_activity("PDF Downloaded")

log_activity("Email Report Created")

log_activity("Dashboard Viewed")

cursor.execute("SELECT * FROM ActivityLog")

rows = cursor.fetchall()

print("="*50)

print("ACTIVITY LOG")

print("="*50)

for row in rows:

    print(row)

conn.close()