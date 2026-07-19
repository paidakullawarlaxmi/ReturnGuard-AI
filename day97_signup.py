from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# ===========================
# Create Database
# ===========================

conn = sqlite3.connect("../database/returnguard.db")

cursor = conn.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS Users(

id INTEGER PRIMARY KEY AUTOINCREMENT,

username TEXT UNIQUE,

password TEXT

)

""")

conn.commit()

conn.close()


# ===========================
# Signup Page
# ===========================

@app.route("/")
def home():

    return render_template("signup.html")


# ===========================
# Register User
# ===========================

@app.route("/signup", methods=["POST"])
def signup():

    username = request.form["username"]

    password = request.form["password"]

    conn = sqlite3.connect("../database/returnguard.db")

    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM Users WHERE username=?",

        (username,)

    )

    user = cursor.fetchone()

    if user:

        conn.close()

        return """

        <h2>User Already Exists</h2>

        <a href="/">Back</a>

        """

    cursor.execute(

        "INSERT INTO Users(username,password) VALUES(?,?)",

        (username,password)

    )

    conn.commit()

    conn.close()

    return """

    <h2>Registration Successful</h2>

    <a href="/loginpage">Go To Login</a>

    """


# ===========================
# Login Page
# ===========================

@app.route("/loginpage")
def loginpage():

    return render_template("login.html")


# ===========================
# Login
# ===========================

@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]

    password = request.form["password"]

    conn = sqlite3.connect("../database/returnguard.db")

    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM Users WHERE username=? AND password=?",

        (username,password)

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

        <a href="/loginpage">Try Again</a>

        """


# ===========================
# Run Flask
# ===========================

if __name__=="__main__":

    app.run(debug=True)