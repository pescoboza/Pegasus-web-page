from flask import redirect, url_for, render_template
from .. import app, db
from ..models.user import User
from decorators import check_is_authenticated

@app.route("/profile/<username>", methods=["GET", "POST"])
@login_required
@check_is_authenticated
def profile(username):
    user = db.session.query(User).filter(User.username == username).firs()
    if user == None:
        redirect(url_for("not_found"))
    render_template("profile.html",user=user)