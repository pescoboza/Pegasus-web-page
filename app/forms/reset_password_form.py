from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms.validators import Required, Length, EqualTo
from ..models import FIELD_LENGTHS as flen


class ResetPasswordForm(FlaskForm):
    password = PasswordField(label="Password", validators=[
                                   Required(), 
                                   Length(**flen["password"])])
    
    repeat_password = PasswordField(label="Password", validators=[
                                   Required(),  
                                   EqualTo("password", 
                                   message="Passwords must match.")])
