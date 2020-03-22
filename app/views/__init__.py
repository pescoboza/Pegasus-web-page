from flask import render_template, redirect, request
from ..models.user import User
from .. import app, db
from ..forms.login_form import LoginForm
from ..forms.sign_up_form import SignUpForm

from .login import *
from .sign_up import *

# ---------------------------------------------------
# Index page
# ---------------------------------------------------
@app.route('/')
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")





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