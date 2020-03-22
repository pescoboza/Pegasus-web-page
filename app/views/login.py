from flask import render_template, request
from .. import app, db
from ..models.user import User
from ..forms.login_form import LoginForm

# ---------------------------------------------------
# Login page
# ---------------------------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()
    message = None

    # Check for a POST request
    if request.method == "POST" and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        # Query for the user with that username
        user =  db.session.query(User).filter(User.username == username).first()
        # Check the password
        if user and user.password == password:
            # TODO: Keep track of the logged in user in the current session
            # TODO: Add logout option
            return render_template("index.html", user=user)

        message = "Invalid credentials. Please try again."
        

    return render_template("login.html", form=form, message=message)