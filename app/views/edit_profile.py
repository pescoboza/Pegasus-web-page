from flask import flash, render_template, redirect, url_for
from flask_login import login_required, current_user
from .. import app
from ..user import User
from ..forms.edit_profile_form import EditProfileForm
import ..profile 

@app.route("/edit-profile", methods=["GET","POST"])
@login_required
def edit_profile():
    form = EditProfileForm()

    if form.validate_on_submit():
        # Update modified information by the user
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data

        db.session.add(current_user)
        db.session.commit()

        flash("Your profile has been updated")

        return redirect(url_for(".profile", username=current_user.username))

    form.first_name.data = current_user.first_name
    form.last_name.data = current_user.last_name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me

    return render_template("profile.html", form=form)