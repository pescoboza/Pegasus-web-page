from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField

class ChatForm(FlaskForm):
    user_response = TextField()
    submit = SubmitField("Send")