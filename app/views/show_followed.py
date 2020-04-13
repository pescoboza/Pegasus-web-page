from flask import make_response, redirect, url_for
from flask_login import login_required
from .. import app
from . import COOKIE_DURATION

@app.route("/followed")
def show_followed():
    resp = make_response(redirect(url_for("blog")))
    resp.set_cookie("show_followed", '1', max_age=COOKIE_DURATION)
    return resp
