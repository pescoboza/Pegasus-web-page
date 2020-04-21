from flask import make_response, redirect, url_for
from flask_login import fresh_login_required
from . import COOKIE_DURATION
from .. import app

# TODO: Add cookies message.

@app.route("/all")
@fresh_login_required
def show_all():
    resp = make_response(redirect(url_for("blog")))
    resp.set_cookie("show_followed", '', max_age=COOKIE_DURATION)
    return resp