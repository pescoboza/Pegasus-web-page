from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import Required, Length, Email, EqualTo
from ..models import FIELD_LENGTHS as flen

class RequestPasswordChangeForm(FlaskForm):
      email = TextField(label="Email", validators=[
                      Required(), Length(**flen["email"]), Email()])