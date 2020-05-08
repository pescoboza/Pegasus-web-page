from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Length
from ..validators import FIELD_LENGTHS as flen

class LoginForm(FlaskForm):
    username = TextField(label="Username", validators=[InputRequired()])
    password = PasswordField(label="Password", validators=[InputRequired()])
    remember = BooleanField(label="Remember Me")

    submit = SubmitField("Login")