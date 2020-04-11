from werkzeug.urls import url_parse
from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_user
from .. import app, db
from ..models.user import User
from ..forms.login_form import LoginForm

# ---------------------------------------------------
# Login page
# ---------------------------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():

    # Unauthenthicated users will be returned to the index page.
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    
    form = LoginForm()

    show_error_invalid_credentials = False

    if form.validate_on_submit():
        user = db.session.query(User).filter(User.username == form.username.data).first()
        
        if user == None or not user.check_password(form.password.data):
            flash("Invalid login credentials.")
            return redirect(url_for("login"))
        
        login_user(user, remember=form.remember.data)
        next_page = request.args.get("next")

        # If the next page is not relative, return the user to index.
        if not next_page or url_parse(next_page).netloc !=  ' ':
            next_page = url_for("index")

        return redirect(next_page)

    return render_template("login.html", title="Login",form=form)