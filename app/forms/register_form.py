from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length, Email

class RegisterForm(FlaskForm):
    first_name = TextField(label="First Name", validators=[
                          InputRequired(), Length(**flen["first_name"])])
    last_name = TextField(label="Last Name", validators=[
                         InputRequired(), Length(**flen["last_name"])])
    username = TextField(label="Username", validators=[
                         InputRequired(), Length(**flen["username"])])
    email = TextField(label="Email", validators=[
                      InputRequired(), Length(**flen["email"])])

    password = PasswordField(label="Password", validators=[
                                   InputRequired(), Length(**flen["password"])])
    repeat_password = PasswordField(label="Password", validators=[
                                   InputRequired(), Length(**flen["password"])])

    newsletter = BooleanField()
    accept_terms_and_conditions = BooleanField()
