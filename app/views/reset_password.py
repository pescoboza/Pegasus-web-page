from flask import render_template, request, redirect, url_for, flash
from passlib.hash import sha256_crypt
from .. import app, db
from ..models.user import User
from ..forms.reset_password_form import ResetPasswordForm
from ..token import confirm_token


# The page with the form in which the actual password is sent.
@app.route("/reset-password/<email>/<token>", methods=["GET", "POST"])
def reset_password(token, email):

    if not confirm_token(token):
        redirect(url_for("not_found"))

    form = ResetPasswordForm()

    if request.method == "POST" and form.validate_on_submit():
        password = form.password.data
        password = sha256_crypt.hash(password)
        # TODO: Manage 404 case.
        user = db.session.query(User).filter(User.email == email).first()

        if user == None:
            return redirect(url_for("not_found"))
        user.password = password
        db.session.add(user)
        db.session.commit()
        flash("Your account's password has been reset.", "success")
        return redirect(url_for("login"))
        
    return render_template("reset_password.html", form=form)

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ #
    #         TODO: FIX PASSWORD RESET SYSTEM         #
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ #