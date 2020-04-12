from flask import render_template, flash, redirect, url_for, current_app, request
from flask_login import current_user
from ..models.post import Post
from .. import app, db
from ..forms.comment_form import CommentForm
from ..models.comment import Comment


@app.route("/post/<int:id>", methods=["GET", "POST"])
def post(id):
    post = Post.query.get_or_404(id)
    form = CommentForm()

    if form.validate_on_submit():
        comment = Comment(body=form.body.data, post=post,
                          author=current_user._get_current_object())
        db.session.add(comment)
        db.session.commit()
        flash("Your comment has been published.")
        return redirect(url_for("post", id=post.id, page=-1))
    
    page = request.args.get("page", 1, type=int)
    if page == -1:
        page = (post.comments.count() -
                1) // current_app.config["APP_COMMENTS_PER_PAGE"] + 1

    pagination = post.comments.order_by(Comment.timestamp.asc()).paginate(
        page, per_page=current_app.config["APP_COMMENTS_PER_PAGE"], error_out=False)
    comments = pagination.items
    return render_template("post.html", posts=[post], form=form, comments=comments, pagination=pagination)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ #
#       TODO: UPDATE BLOG.PY TO SHOW COMMENTS         #
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ #