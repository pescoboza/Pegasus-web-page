from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    body = TextAreaField("What do you want to share?", validators=[DataRequired()])
    submit = SubmitField()