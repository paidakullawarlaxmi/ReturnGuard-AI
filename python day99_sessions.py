from flask import session
app.secret_key = "returnguard_secret_key"
session["username"] = username
@app.route("/dashboard")
def dashboard():

    if "username" in session:

        return render_template(
            "dashboard.html",
            username=session["username"]
        )

    return redirect("/loginpage")
@app.route("/logout")
def logout():

    session.pop("username", None)

    return redirect("/loginpage")