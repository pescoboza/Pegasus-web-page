from flask import render_template, redirect, request, flash
from ..models.user import User
from .. import app, db
from ..forms.login_form import LoginForm
from ..forms.register_form import RegisterForm

from .login import *
from .user_confirmation import *
from .register import *


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
