from flask import redirect, url_for
from flask_login import logout_user
from .. import app

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))