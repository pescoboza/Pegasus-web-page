from datetime import datetime
from flask import render_template, redirect, flash, url_for, request, session
from .. import app, db
from ..models.user import User
from ..forms.register_form import RegisterForm
from ..token import generate_confirmation_token
from .user_confirmation import user_confirmation
from ..send_email import send_email
import sys

# ---------------------------------------------------
# Sign up page
# ---------------------------------------------------
@app.route("/register", methods=["GET", "POST"])
@app.route("/sign-up", methods=["GET", "POST"])
def register():

    form = RegisterForm()

    # TODO: Add validation for matching password with repeated password
    if request.method == "POST" and form.validate_on_submit():
        validation_error = False

        # Check if email is available
        if db.session.query(User).filter(User.email == form.email.data).first() != None:
            form.email.errors.append("That email address is already registered.")
            validation_error = True

        # Check if username is available
        if db.session.query(User).filter(User.username == form.username.data).first() != None:
            form.username.errors.append("That username is already taken.")
            validation_error = True

        # Database validation failed, return the form with respective errors
        if not validation_error:
            # Createa a new user object
            new_user = User(
                form.first_name.data,
                form.last_name.data,
                form.email.data,
                form.username.data,
                form.password.data,
                datetime.now(),
                form.newsletter.data)

            # Add the new user to the database
            db.session.add(new_user)
            db.session.commit()

            # Generation of confirmation email
            token = generate_confirmation_token(new_user.email)
            confirm_url = url_for("user_confirmation",token=token, _external=True)
            html = render_template("user_confirmation.html", 
                                confirm_url=confirm_url)
            subject = "Pegasus: please confirm your email!"
            status = send_email(subject=subject, recipients=[new_user.email], html_body=html)
            
            flash("A confirmation email has been sent to your email.","success")
            return redirect(url_for("index"))

    return render_template("register.html", form=form)

# TODO: Figure out how to send confiration emails. 
# TODO: Figure out how to correctly display flashes.