from datetime import datetime
from flask import render_template, redirect, url_for, request, session
from passlib.hash import sha256_crypt
from .. import app, db
from ..models.user import User
from ..forms.register_form import RegisterForm     
from ..token import generate_confirmation_token
from .user_confirmation import user_confirmation

# ---------------------------------------------------
# Sign up page
# ---------------------------------------------------
@app.route("/register", methods=["GET","POST"])
@app.route("/sign-up", methods=["GET","POST"])
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
                sha256_crypt.hash(form.password.data), 
                datetime.now())  

            # TODO: Add email confirmation to user registration
            
            # Add the new user to the database
            db.session.add(new_user)
            db.session.commit()

            token = generate_confirmation_token(new_user.email)

            return user_confirmation()

    return render_template("sign_up.html", form=form)