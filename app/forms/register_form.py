from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import Required, Length, Email, EqualTo
from ..models import FIELD_LENGTHS as flen

class RegisterForm(FlaskForm):
    first_name = TextField(label="First Name", validators=[
                          Required(), Length(**flen["first_name"])])
    last_name = TextField(label="Last Name", validators=[
                         Required(), Length(**flen["last_name"])])
    username = TextField(label="Username", validators=[
                         Required(), Length(**flen["username"])])
    email = TextField(label="Email", validators=[
                      Required(), Length(**flen["email"]), Email()])

    password = PasswordField(label="Password", validators=[
                                   Required(), 
                                   Length(**flen["password"])])
    repeat_password = PasswordField(label="Password", validators=[
                                   Required(),  
                                   EqualTo("password", 
                                   message="Passwords must match.")])

    newsletter = BooleanField()
    accept_terms_and_conditions = BooleanField(validators=[Required()])
