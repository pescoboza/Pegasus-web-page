from flask_wtf import FlaskForm
from wtforms improt Textfield, Password

class LoginForm(FlaskForm):
    username = TextField("username")
    password = TextField("password")