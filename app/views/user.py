from flask import render_template
from .. import app
from ..models.user import User

@app.route("user/<username>")
def user(username):
    user = User.query.filter_by(username=username).first()
    if user == None:
        abort(404)
    posts = user.posts.order_by(Post.timestamp.desc()).all()
    return render_template("user.html", user=user)