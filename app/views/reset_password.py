from flask import request, redirect, url_for, flash
from passlib.hash import sha256_crypt
from .. import app, db
from ..models.user import User
from ..forms.reset_password_form import ResetPasswordForm


# The page with the form in which the actual password is sent.
@app.route("/reset-password/<token>", methods=["GET", "POST"])
def reset_password(username):
    form = ResetPasswordForm()

    if request.method == "POST" and form.validate_on_submit():
        password = form.password.data
        password = sha256_crypt.hash(password)
        user = db.session.query(User).filter(User.username == username).first()

        if user == None:
            return redirect(url_for("not_found"))
        user.password = password
        db.session.add(user)
        db.session.commit()
        flash("Your account's password has been reset.", "success")
        redirect(url_for("login"))
    
    render_template("reset_password.html", form=form)