from flask import render_template
from ..models.post import Post
from .. import app

@app.route("/post/<int:id>", methods=["GET", "POST"])
def post(id):
    post = Post.query.get_or_404(id)
    return render_template("post.html", posts=[post])