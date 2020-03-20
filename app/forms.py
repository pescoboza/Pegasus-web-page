from flask_wtf import FlaskForm
import wtforms
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length, Email
import copy

fields = {
    "username":
     lambda required=True: TextField(label="Username",  
                validators=[Length(min=8, max=16), InputRequired() if required else None]),
    "password": 
    lambda required=True: PasswordField(label="Password",
                validators=[Length(min=8, max=60), InputRequired() if required else None]),
    "email":
    lambda required=True: TextField(label="Email",
                validators=[InputRequired() if required else None]),
}


class LoginForm(FlaskForm):
    username = fields["username"]()

    password = fields["password"]()
    remember = BooleanField()


class RegisterForm(FlaskForm):
    username = fields["username"]()
    
    password = fields["password"]()
    enter_password_again = fields["password"]()

