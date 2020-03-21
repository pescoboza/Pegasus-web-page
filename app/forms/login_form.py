from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length
from ..models import FIELD_LENGTHS as flen

class LoginForm(FlaskForm):
    username = TextField(label="Username", validators=[
                         InputRequired(), Length(**flen["username"])])
    password = PasswordField(label="Password", validators=[
                             InputRequired(), Length(**flen["password"])])
    remember = BooleanField()