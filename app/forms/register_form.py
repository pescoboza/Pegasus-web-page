from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length, Email, EqualTo
from .. import db
from ..validators import create_new_field
from ..models.user import User

class RegisterForm(FlaskForm):
    first_name = create_new_field("first_name")
    last_name = create_new_field("last_name")
    username = create_new_field("username")
    email = create_new_field("email")
    password = create_new_field("password")
    repeat_password = PasswordField(label="Repeat password", validators=[
                                   DataRequired(),  
                                   EqualTo("password", 
                                   message="Passwords must match.")])

    newsletter = BooleanField()
    accept_terms_and_conditions = BooleanField(validators=[DataRequired()])

    submit = SubmitField("Register")

    def validate_username(self, username):
        user = db.session.query(User).filter(User.username == username.data).first()
        if user != None:
            raise ValidationError("Please choose a different username.")

    def validate_email(self, email):
        user = db.session.query(User).filter(User.email == email.data).first()
        if user != None:
            raise ValidationError("Please use a different email address.")
