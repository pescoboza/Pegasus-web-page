from functools import wraps
from flask import flash, redirect, url_for
from flask.ext.login import current_user

def check_confirmed(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.confirmed is False:
            flash("Please confirm your account.","warning")
            return redirect(url_for("user.unconfirmed"))
        return func(*args, **kwargs)
    
    return decorated_function

# Checks that the user is logged in, else it redirects to login page
def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return func(*args, **kwargs)
        else:
            flash("Please login to continue.")
            return redirect(url_for("/login"))
