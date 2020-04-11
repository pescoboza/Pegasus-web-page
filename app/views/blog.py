from flask import request, render_template, flash, redirect, url_for, current_app
from flask_login import current_user
from .. import app, db
from ..forms.post_form import PostForm
from ..models.user import Permission
from ..models.post import Post

@app.route("/blog", methods=["GET", "POST"])
def blog():
    form = PostForm()

    can_write_articles = False
    try:
        can_write_articles = current_user.can(Permission.WRITE_ARTICLES) 
    except AttributeError:
        can_write_articles = False

    # TODO: Add role of blogger
    if can_write_articles and form.validate_on_submit():
        post = Post(body=form.body.data,
                    author=current_user._get_current_object())
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("blog"))

    page = request.args.get("page", 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config["APP_POSTS_PER_PAGE"],
        error_out=False)
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template("blog.html", form=form, posts=posts, Permission=Permission, pagination=pagination)
    