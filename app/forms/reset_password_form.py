from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
from ..validators import FIELD_LENGTHS as flen


class ResetPasswordForm(FlaskForm):
    password = PasswordField(label="New password", validators=[
                                   DataRequired(), 
                                   Length(**flen["password"])])
    
    repeat_password = PasswordField(label="Repeat password", validators=[
                                   DataRequired(),  
                                   EqualTo("password", 
                                   message="Passwords must match.")])

    submit = SubmitField("Submit")
