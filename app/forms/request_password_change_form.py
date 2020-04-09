from flask_wtf import FlaskForm
from wtforms import ValidationError, TextField, SubmitField
from wtforms.validators import Required, Length, Email, EqualTo
from .. import db
from ..validators import FIELD_LENGTHS as flen
from ..models.user import User

class RequestPasswordChangeForm(FlaskForm):
      email = TextField(label="Email", validators=[
                      Required(), Length(**flen["email"]), Email()])
      submit = SubmitField("Submit")