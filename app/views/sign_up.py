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

    # TODO: Add validation for matching password with repeated password
    if request.method == "POST" and form.validate_on_submit():
        new_user = User(
            form.first_name,
            form.last_name,
            form.email,
            form.username,
            form.password, 
            datetime.now().ctime())

        email_available = bool(db.session.query(User).filter(User.email == new_user.email).count() == 0)
        username_available = bool(db.session.query(User).filter(User.username == new_user).count() == 0)