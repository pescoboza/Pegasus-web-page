from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError,Required, Length, Email, EqualTo
from .. import db
from ..validators import NEW_FIELDS as nf
from ..models.user import User

class RegisterForm(FlaskForm):
    first_name = nf["first_name"]
    last_name = nf["last_name"]
    username = nf["username"]
    email = nf["email"]
    password = nf["password"]
    repeat_password = PasswordField(label="Repeat password", validators=[
                                   Required(),  
                                   EqualTo("password", 
                                   message="Passwords must match.")])

    newsletter = BooleanField()
    accept_terms_and_conditions = BooleanField(validators=[Required()])

    submit = SubmitField("Register")

    def validate_username(self, username):
        user = db.session.query(User).filter(User.username == username.data).first()
        if user != None:
            raise ValidationError("Please choose a different username.")

    def validate_email(self, email):
        user = db.session.query(User).filter(User.email == email.data).first()
        if user != None:
            raise ValidationError("Please use a different email address.")
