from ..models.user import User
from token import generate_confirmation_token


@app.route("/resend")
@login_required

def resend_confirmation():
    token = generate_confirmation_token(current_user.email)
    confirm_url = url_for("user.confirm_email", token=token,_external=True)
    html = render_template("user/activate.html", confirm_url=confirm_url)