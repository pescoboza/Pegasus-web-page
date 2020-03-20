from flask import render_template, redirect, url_for, flash
from app import app
from models import *
from forms import LoginForm

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

    form = LoginForm()

    if form.validate_on_submit():
        return redirect(url_for("/home"))

    return render_template("auth/login.html", form=form)
    #error = None

    # user = {
    #     "username": "lolo23jhon",
    #     "password": "pegasus"
    # }

    # # TODO: Connect validation to database
    # if request.method == "POST":
    #     username = request.form["username"]
    #     password = request.form["password"]

    #     if username == user["username"] and password == user["password"]:
    #         # TODO: Change redirection after succesful login
    #         return redirect(url_for("index"))
    #     else:
    #         error = "Invalid Credentials. Please ty again."

    # return render_template("auth/login.html", error=error)


# ---------------------------------------------------
# Profile page
# ---------------------------------------------------
@app.route("/user/<username>")
def profile(username):
    return render_template("profile.html")


# ---------------------------------------------------
# Testing development page
# ---------------------------------------------------
@app.route("/dev-all-members")
def all_members():
    page = str()
    line =  "<h1>{}</h1><br>"
    for i in range(10):
        page += line.format(i)
    return page