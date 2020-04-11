from flask import render_template, abort, redirect, url_for, flash
from flask_login import login_required, current_user
from .. import app, db
from ..models.user import User, Permission
from ..models.post import Post
from ..forms.post_form import PostForm

@app.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit(id):
    post = Post.query.get_or_404(id)

    if current_user != post.author and not current_user.can(Permission.ADMIN):
        abort(403)

    form = PostForm()

    if form.validate_on_submit():
        post.body = form.body.data
        db.session.add(post)
        db.session.commit()
        flash("The post has been updated.")
        return redirect(url_for(".post", id=id))
    form.body.data = post.body
    return render_template("edit_post.html", form=form)