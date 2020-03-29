from flask_wtf import FlaskForm
from wtforms import TextField

class ChatForm(FlaskForm):
    user_response = TextField()