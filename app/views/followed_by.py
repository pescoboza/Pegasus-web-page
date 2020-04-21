from flask import render_template, redirect, url_for, flash, request, current_app
from .. import app
from ..models.user import User


@app.route("/followed_by/<username>")
def followed_by(username):
    user = User.query.filter_by(username=username).first()
    if user == None:
        flash("Invalid user.")
        return redirect(url_for("index"))

    page = request.args.get("page", 1, type=int)
    pagination = user.followed_by.paginate(page, per_page=current_app.config["APP_FOLLOWERS_PER_PAGE"], error_out=False)
    follows = [{"user": item.follower, "timestamp": item.timestamp} for item in pagination.items]

    return render_template("followers.html", user=user, title="Followers of", endpoint="followers", pagination=pagination, follows=follows)