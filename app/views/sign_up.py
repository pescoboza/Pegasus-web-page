from datetime import datetime
from flask import render_template, request
from .. import app, db
from ..models.user import User
from ..forms.sign_up_form import SignUpForm

# ---------------------------------------------------
# Sign up page
# ---------------------------------------------------
@app.route("/sign-up", methods=["GET","POST"])
def sign_up():

    form = SignUpForm()
    validation_error = False
    new_user = None

    # TODO: Add validation for matching password with repeated password
    if request.method == "POST" and form.validate_on_submit():
        new_user = User(
            form.first_name,
            form.last_name,
            form.email,
            form.username,
            form.password, 
            datetime.now().ctime())


        # Check if email is available
        if db.session.query(User).filter(User.email == new_user.email).count() != 0:
            form.email.errors.append("That email address is already registered.")
            validation_error = True

        # Check if username is available
        if db.session.query(User).filter(User.username == new_user).count() != 0:
            form.username.errors.append("That username is already taken.")
            validation_error = True

    if validation_error:
        return render_template("sign_up.html", form=form)
    
    # TODO: Add email confirmation to user registration
    # No error, add new user to database
    db.session.add(new_user)
    db.session.commit()

    return render_template("index.html", username=new_user)