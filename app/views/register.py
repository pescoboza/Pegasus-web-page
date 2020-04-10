from datetime import datetime
from flask import render_template, redirect, flash, url_for, request, session
from .. import app, db
from ..models.user import User
from ..forms.register_form import RegisterForm
from ..token import generate_confirmation_token
from .user_confirmation import user_confirmation
from ..send_email import send_email

# ---------------------------------------------------
# Sign up page
# ---------------------------------------------------
@app.route("/register", methods=["GET", "POST"])
def register():

    form = RegisterForm()

    # TODO: Add validation for matching password with repeated password
    if form.validate_on_submit():

        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            username=form.username.data,
            password=form.password.data,
            registered_on=datetime.utcnow(),
            newsletter=form.newsletter.data)

        db.session.add(new_user)
        db.session.commit()

        # Generation of confirmation email
        token = generate_confirmation_token(new_user.email)
        confirm_url = url_for("user_confirmation", token=token, _external=True)
        html = render_template("user_confirmation.html",
                               confirm_url=confirm_url)

        subject = "Pegasus: please confirm your email!"
        status = send_email(subject=subject, recipients=[
                            new_user.email], html_body=html)

        flash("A confirmation email has been sent to your email.", "success")
        return redirect(url_for("index"))

    return render_template("register.html", form=form)