from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import Required, Length, EqualTo
from ..models import FIELD_LENGTHS as flen


class ResetPasswordForm(FlaskForm):
    password = PasswordField(label="New password", validators=[
                                   Required(), 
                                   Length(**flen["password"])])
    
    repeat_password = PasswordField(label="Repeat password", validators=[
                                   Required(),  
                                   EqualTo("password", 
                                   message="Passwords must match.")])

    submit = SubmitField("Submit")
