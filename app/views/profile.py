from decorators import check_confirmed


@app.route("/profile", methods=["GET", "POST"])
@login_required
@check_confirmed
def profile():