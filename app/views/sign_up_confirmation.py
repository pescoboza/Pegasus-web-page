from flask import render_template
from .. import app

@app.route("/sign-up-confirmation")
def signup_confirmation(): 
    message = "Thank you for registering.\n To activate your account, check your email and click on the confirmation link.".format(new_user.username, cover_email(new_user.email))
    return render_template("message.html", message=message)