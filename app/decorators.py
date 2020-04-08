from functools import wraps
from flask import flash, redirect, url_for, session
from flask_login import current_user
from . import db
from .models.user import User
from .models.roles import Permission

def check_is_authenticated(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        user = db.session.query(User).filter(User.username == session["username"]).first_or_404()
        if user.is_authenticated == False:
            flash("Please confirm your account.","warning")
            return redirect(url_for("confirm"))
        return func(*args, **kwargs)
    return decorated_function

def permission_required(permission):
    def decortor(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# If the user is admin it proceeds, else it sends you to the homepage silently
def admin_required(func):
    return permission_required(Permission.ADMIN)(func)

def moderator_required(func)
    return permission_required(Permission.MODERATE)(func)