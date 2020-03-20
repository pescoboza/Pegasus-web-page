from flask_wtf import FlaskForm
import wtforms
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):
    username = TextField(label="Username", 
                        validators=[InputRequired(),Length(min=8, max=16)])

    password = PasswordField(label="Password",
                             validators=[InputRequired(), Length(min=8, max=60)], description="feferef")
    remember = BooleanField()
