from flask import render_template
from .. import app
from ..models.user import User

@app.route("user/<username>")
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template("user.html", user=user)