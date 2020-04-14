from flask import  flash, redirect, url_for
from flask_login import fresh_login_required, current_user
from .. import app, db
from ..decorators import permission_required
from ..models.user import Permission, User

@app.route("/follow/<username>", methods=["GET", "POST"])
@fresh_login_required
@permission_required(Permission.FOLLOW)
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user == None:
        flash("Invalid user.")
        return redirect(url_for("index"))
    
    if current_user.is_following(user):
        flash("You are already following this user.")
        return redirect(url_for("user", username=username))
    
    current_user.follow(user)
    db.commit()
    flash("You are now following {username}".format(username=username))
    return redirect(url_for("user", username=username))