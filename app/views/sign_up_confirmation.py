from datetime import datetime
from flask import render_template, flash, redirect, url_for
from ..models.user import User
from ..token import generate_confirmation_token, confirm_token
from .. import app, db

@app.route("/confirm/<token>")
@login_required # TODO: Add decorators
def confirm_email(token): 
    try: 
        email = confirm_token(token)
    except:
        flash("The confirmation link is invalid or has expired","danger")
    
    user = db.session.query(User).filter(User.email == email).first_or_404()
    if user.confirmed:
        flash("Acount already confirmed. Please login.","success")
    else:
        user.confirmed = True
        user.confirmed_on = datetime.now().ctime()
        db.session.add(user)
        db.session.commit()
        flash("You succesfully confirmed your account. Thank you!","success")
    return redirect(url_for("/home"))