from datetime import datetime
from flask import render_template, redirect, url_for, request
from .. import app, db
from ..models.user import User
from ..forms.sign_up_form import SignUpForm
from .sign_up_confirmation import *

# ---------------------------------------------------
# Sign up page
# ---------------------------------------------------
@app.route("/sign-up", methods=["GET","POST"])
def sign_up():

    form = SignUpForm()   
    
    # TODO: Add validation for matching password with repeated password
    if request.method == "POST" and form.validate_on_submit():
        validation_error = False

        # Check if email is available
        if db.session.query(User).filter(User.email == form.email).count() != 0:
            form.email.errors.append("That email address is already registered.")
            validation_error = True

        # Check if username is available
        if db.session.query(User).filter(User.username == form.username).count() != 0:
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
                datetime.now().ctime())  

            # TODO: Add email confirmation to user registration
            # Add the new user to the database
            db.session.add(new_user)
            db.session.commit()

            return sign_up_confirmation()

    return render_template("sign_up.html", form=form)
