from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import Email, DataRequired, Length, ValidationError
from ..models.user import User
from ..validators import create_new_field

# TODO: Add roles
class EditProfileAdminForm(FlaskForm):
    email = create_new_field("email")
    username = create_new_field("username")
    first_name = create_new_field("first_name")
    last_name = create_new_field("last_name")
    confirmed = BooleanField("Confirmed")
    location = create_new_field("location")
    about_me = create_new_field("about_me")

    submit = SubmitField("Submit")

    role = SelectField("Role", coerce=int)

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name)]

        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already registered.")

    def validate_username(self, field):
        if field.data != self.user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already in usage.")