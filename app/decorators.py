from functools import wraps
from flask import flash, redirect, url_for, session
from . import db
from .models.user import User

def check_confirmed(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.confirmed == False:
            flash("Please confirm your account.","warning")
            return redirect(url_for("/confirm"))
        return func(*args, **kwargs)
    return decorated_function

# Checks that the user is logged in, else it redirects to login page
def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if session["logged_in"] == True:
            return func(*args, **kwargs)
        else:
            flash("Please login to continue.")
            return redirect(url_for("/login"))
    return decorated_function

# If the user is admin it proceeds, else it sends you to the homepage silently
def admin_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        user = User.query.filter_by(username=usename).first()
        if user != None and user.admin == True:
            return func(*args, **kwargs)
        else:
            return redirect(url_for("/home"))
    return decorated_function