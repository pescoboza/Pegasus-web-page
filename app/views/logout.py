from flask import flash, redirect, url_for
from .. import app
from ..decorators import login_required


@app.route("/logout")
@login_required
def logout():
    session.clear()
    flash("Use logged out.")
    # TODO: Add garbage collector
    return redirect(url_for("/home"))