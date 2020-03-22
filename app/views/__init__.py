from flask import render_template, redirect, request
from ..models.user import User
from .. import app, db
from ..forms.login_form import LoginForm
from ..forms.sign_up_form import SignUpForm

from .login import *
from .sign_up import *


# ---------------------------------------------------
# Helpers
# ---------------------------------------------------
class Button:
    # To be used with:
    """
    <form action="{{button.action}}">
        <input type="submit" value="{{button.value}}">
    </form>
    """
    __init__(self, value, action):
        self.link = link
        self.text = text

def cover_email(email,num_visible_chars=1, replacement_char='*'):
    at = email.find('@')
    uname = email[:at]
    not_uname = email[at:]
    uncovered_part = uname[:num_visible_chars]
    if len(uname) <= num_visible_chars:
        raise ValueError("Email username must be longer than the number of covered characters. Got {} and expected al least {}".format(len(uname), num_visible_chars+1))
    
    return  uncovered_part + (len(uname)-num_visible_chars)*replacement_char + not_uname
        
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