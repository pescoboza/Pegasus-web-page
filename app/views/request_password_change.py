from flask import render_template, request, redirect, url_for
from . import app, db
from ..models.user import User
from ..forms.request_password_change_form import RequestPasswordChangeForm
from ..token import generate_confirmation_token
from ..send_email import send_email

@app.route("/forgot-password", request=["POST"])
def request_password_change():
    form = RequestPasswordChangeForm()

    if request == "POST" and form.validate_on_submit():
        email = form.email.data
        user = db.session.query(User).filter(User.email == email).first()

        if user != None:
            token = generate_confirmation_token(user.email)
            confirmation_url = url_for( "reset-password", url=token, _external=True)
            
            text_body = "We received a request from you to reset your password. Please follow the link to do so:\n" + confirmation_url
            html_body = render_template("password_reset_confirmation_email.html", confirmation_url=confirmation_url)

            send_email("Password change request.", [user.email], text_body=text_body, html_body=html_body)
        flash("A password rest token has been sent to your email.")
    
    render_template("password_reset.html" , form=form)