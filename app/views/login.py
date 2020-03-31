from flask import render_template, request, flash, session
from .. import app, db
from ..models.user import User
from ..forms.login_form import LoginForm
from passlib.hash import sha256_crypt
from time import sleep
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

        # Check username
        if user != None:
        
            # Check if account confirmed
            if user.confirmed == True:
                
                # Check if password correct
                if sha256_crypt.verify(password,user.password):
                
                    # TODO: Add logout option session.
                    session["logged_in"] = True
                    session["username"] = username
                    
                    # Login succesful
                    return render_template("index.html", user=user)
            else:
                flash("Please confirm your account.")
        else:
            flash("Invalid credentials. Please try again.")
        
    return render_template("login.html", form=form)