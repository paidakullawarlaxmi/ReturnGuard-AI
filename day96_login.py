from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Create Database
conn = sqlite3.connect("../database/returnguard.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(

id INTEGER PRIMARY KEY AUTOINCREMENT,

username TEXT UNIQUE,

password TEXT

)
""")

# Insert Default User Only Once
cursor.execute("SELECT * FROM Users WHERE username='admin'")

user = cursor.fetchone()

if user is None:

    cursor.execute("""

    INSERT INTO Users(username,password)

    VALUES

    ('admin','admin123')

    """)

    conn.commit()

conn.close()


@app.route("/")
def home():

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]

    password = request.form["password"]

    conn = sqlite3.connect("../database/returnguard.db")

    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM Users WHERE username=? AND password=?",

        (username, password)

    )

    user = cursor.fetchone()

    conn.close()

    if user:

        return render_template(

            "dashboard.html",

            username=username

        )

    else:

        return """

        <h2>Invalid Username or Password</h2>

        <a href="/">Try Again</a>

        """


if __name__ == "__main__":

    app.run(debug=True)