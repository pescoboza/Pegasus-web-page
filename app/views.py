from flask import render_template, redirect, request, url_for
from app import app

# ---------------------------------------------------
# Index page
# ---------------------------------------------------
@app.route('/')
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")

# ---------------------------------------------------
# Login page
# ---------------------------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():

    error = None

    user = {
        "username": "lolo23jhon",
        "password": "pegasus"
    }

    # TODO: Connect validation to database
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == user["username"] and password == user["password"]:
            # TODO: Change redirection after succesful login
            return redirect(url_for("index"))
        else:
            error = "Invalid Credentials. Please ty again."

    return render_template("auth/login.html", error=error)


# ---------------------------------------------------
# Profile page
# ---------------------------------------------------
@app.route("/user/<username>")
def profile(username):
    return render_template("profile.html")
