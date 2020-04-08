from flask import request, render_template, flash
from flask_login import current_user
from .. import app
from ..forms.post_form import PostForm

@app.route("/blog", methods=["GET", "POST"])
def blog():
    form = PostForm()
    if current_user.can(Permission.W) # TODO: Continue this: permission of user to post in blog