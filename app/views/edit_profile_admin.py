from flask import flash, redirect, url_for
from flask_login import login_required
from ..decorators import admin_required
from .. import app, db
from ..models.user import User
from ..forms.edit_profile_admin_form import EditProfileAdminForm

@app.route("/edit-profile/<int:id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm()

    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data) # TODO: Add user roles
        user.location = form.location.data
        user.about_me = form.about_me.data

        db.session.add(user)
        db.session.commit()

        flash ("The profile has been updated.")

        return redirect(url_for("/profile", username=user.username))

    form.email.data = user.email
    form.username.data = user.username
    form.first_name.data = user.first_name
    form.last_name.data = user.last_name
    form.location.data = user.location
    form.about_me.data = user.about_me
    form.confirmed.data = user.confirmed
    form.role.data = user.role_id

    return render_template("edit_profile.html", form=form, user=user) # TODO: Write edit_profile.html and add check for if user is administrator