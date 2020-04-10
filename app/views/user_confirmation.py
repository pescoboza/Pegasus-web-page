from datetime import datetime
from flask import render_template, flash, redirect, url_for
from ..models.user import User
from ..token import generate_confirmation_token, confirm_token
from .. import app, db

@app.route("/confirm/<token>")
def user_confirmation(token): 
    try: 
        email = confirm_token(token)
    except:
        flash("The confirmation link is invalid or has expired","danger")
    
    # TODO: Add setting to app for 404 page.
    user = db.session.query(User).filter(User.email == email).first_or_404()
    if user != None and user.is_authenticated:
        flash("Acount already is_authenticated. Please login.","success")
        return redirect(url_for("login"))
    else:
        user.is_authenticated = True
        user.authenticated_on = datetime.utcnow()
        db.session.add(user)
        db.session.commit()
        flash("You succesfully authenticated your account. Thank you!","success")
    return redirect(url_for("index"))