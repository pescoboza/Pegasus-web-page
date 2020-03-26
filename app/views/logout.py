import gc
from flask import flash, redirect, url_for, session
from .. import app
from ..decorators import login_required


@app.route("/logout")
@login_required
def logout():
    session.clear()
    gc.collect()
    return redirect(url_for("/home"))