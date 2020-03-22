from flask import render_template
from .. import app

@app.route("/sign-up-confirmation")
def sign_up_confirmation(): 
    message = "Thank you for registering.\n To activate your account, check your email and click on the confirmation link."
    return render_template("message.html", message=message)