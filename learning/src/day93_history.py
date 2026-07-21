from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def history():

    conn = sqlite3.connect("../database/returnguard.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM FraudHistory")

    rows = cursor.fetchall()

    conn.close()

    return render_template("history.html", data=rows)

if __name__ == "__main__":
    app.run(debug=True)