from flask_wtf import FlaskForm
import wtforms
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length, Email
import copy


FIELD_LENGTHS = {
    "username": {
        "min": 8,
        "max": 16,
        "message": None
    },
    "password": {
        "min": 8,
        "max": 30,
        "message": None
    },
    "firstName": {
        "min": 1,
        "max": 30,
        "message": None
    },
    "lastName": {
        "min": 1,
        "max": 30,
        "message": None
    },
    "email": {
        "min": 5,
        "max": 254,
        "message": None
    },
}

flen = FIELD_LENGTHS

class LoginForm(FlaskForm):
    username = TextField(label="Username", validators=[
                         InputRequired(), Length(**flen["username"])])
    password = PasswordField(label="Password", validators=[
                             InputRequired(), Length(**flen["password"])])
    remember = BooleanField()


class RegisterForm(FlaskForm):
    firstName = TextField(label="First Name", validators=[
                          InputRequired(), Length(**flen["firstName"])])
    lastName = TextField(label="Last Name", validators=[
                         InputRequired(), Length(**flen["lastName"])])
    username = TextField(label="Username", validators=[
                         InputRequired(), Length(**flen["username"])])
    email = TextField(label="Email", validators=[
                      InputRequired(), Length(**flen["email"])])

    password_first = PasswordField(label="Password", validators=[
                                   InputRequired(), Length(**flen["password"])])
    password_again = PasswordField(label="Password", validators=[
                                   InputRequired(), Length(**flen["password"])])

    newsletter = BooleanField()
    accept_terms_and_conditions = BooleanField()
