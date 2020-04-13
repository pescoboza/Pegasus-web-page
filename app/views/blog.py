from flask import request, render_template, flash, redirect, url_for, current_app
from flask_login import current_user
from .. import app, db
from ..forms.post_form import PostForm
from ..models.user import Permission
from ..models.post import Post


@app.route("/blog", methods=["GET", "POST"])
def blog():
    form = PostForm()

    if current_user.can(Permission.WRITE_ARTICLES) and form.validate_on_submit():
        post = Post(body=form.body.data,
                    author=current_user._get_current_object())
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("blog"))

    page = request.args.get("page", 1, type=int)

    show_followed = False
    query = None
    if current_user.is_authenticated:
        show_followed = bool(request.cookies.get("show_followed", ''))

    if show_followed:
        query = current_user.followed_posts
    else:
        query = Post.query

    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config["APP_POSTS_PER_PAGE"],
        error_out=False)
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template("blog.html", form=form, posts=posts, show_followed=show_followed, pagination=pagination)
