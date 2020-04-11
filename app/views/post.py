from flask import render_template
from ..models import Post
from .. import app

def post(id):
    post = Post.query.get_or_404(id)
    return render_template("posts.html", posts=[post])