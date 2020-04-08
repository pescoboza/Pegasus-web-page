from flask import request, redirect, url_for
from flask_login import current_user
from .. import app
from ..models.user import User

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()
        if not current_user.confirmed  and request.endpoint and request.blueprint != "auth" and request.endpoint != "static":
            return redirect(url_for("unconfirmed"))
