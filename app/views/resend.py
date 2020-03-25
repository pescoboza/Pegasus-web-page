from ..models.user import User
from token import generate_confirmation_token
from .send_email import send_email


@app.route("/resend")
@login_required

# TODO: Edit email confirmation
def resend_confirmation(subject):
    # Generate a new token
    token = generate_confirmation_token(current_user.email)
    
    # Generate the temporary url the user will be sent to
    confirm_url = url_for("user.confirm_email", token=token,_external=True)
    
    html = render_template("user/activate.html", confirm_url=confirm_url)
    
    subject = "Please confirm your email"

    send_email(current_user.email, subject)

# message, port, smltp_server, login, password, sender_email, receiver_email, subject