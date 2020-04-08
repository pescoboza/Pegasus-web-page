from functools import wraps
from flask import flash, redirect, url_for, session
from flask_login import current_user
from . import db
from .models.user import User

def check_confirmed(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        user = db.session.query(User).filter(User.username == session["username"]).first_or_404()
        if user.confirmed == False:
            flash("Please confirm your account.","warning")
            return redirect(url_for("confirm"))
        return func(*args, **kwargs)
    return decorated_function

# If the user is admin it proceeds, else it sends you to the homepage silently
def admin_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        user = User.query.filter_by(username=current_user.username).first()
        if user != None and user.is_administrator == True:
            return func(*args, **kwargs)
        else:
            return redirect(url_for("index"))
    return decorated_function