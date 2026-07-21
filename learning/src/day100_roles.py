role = "user"
session["username"] = username
session["role"] = role
if session["role"] != "admin":
    return "Access Denied"