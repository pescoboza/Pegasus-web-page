from flask import request, render_template, flash, redirect, url_for
from flask_login import current_user
from .. import app
from ..forms.post_form import PostForm
from ..models.roles import Permission

@app.route("/blog", methods=["GET", "POST"])
def blog():
    form = PostForm()
    
    # TODO: Add role of blogger
    if current_user.can(Permission.WRITE_ARTICLES) and form.validate_on_submit():
        post = Post(body=form.body.data,
                    author=current_user._get_current_object())
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("blog"))
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template("index.html", form=form, posts=posts)
    