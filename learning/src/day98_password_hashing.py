from flask import Flask, render_template, request
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

#############################################
# CREATE DATABASE
#############################################

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

#############################################
# HOME PAGE
#############################################

@app.route("/")
def home():

    return render_template("signup.html")

#############################################
# SIGNUP
#############################################

@app.route("/signup", methods=["POST"])

def signup():

    username = request.form["username"]

    password = request.form["password"]

    hashed_password = generate_password_hash(password)

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

        <a href="/">Try Again</a>

        """

    cursor.execute(

        "INSERT INTO Users(username,password) VALUES(?,?)",

        (username, hashed_password)

    )

    conn.commit()

    conn.close()

    return """

    <h2>Registration Successful</h2>

    <a href="/loginpage">

    Go To Login

    </a>

    """

#############################################
# LOGIN PAGE
#############################################

@app.route("/loginpage")

def loginpage():

    return render_template("login.html")

#############################################
# LOGIN
#############################################

@app.route("/login", methods=["POST"])

def login():

    username = request.form["username"]

    password = request.form["password"]

    conn = sqlite3.connect("../database/returnguard.db")

    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM Users WHERE username=?",

        (username,)

    )

    user = cursor.fetchone()

    conn.close()

    if user:

        stored_password = user[2]

        if check_password_hash(

            stored_password,

            password

        ):

            return render_template(

                "dashboard.html",

                username=username

            )

    return """

    <h2>Invalid Username or Password</h2>

    <a href="/loginpage">

    Try Again

    </a>

    """

#############################################
# RUN FLASK
#############################################

if __name__=="__main__":

    app.run(debug=True)