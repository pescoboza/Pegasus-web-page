from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Email, DataRequired, Length
from ..models import FIELD_LENGTHS as flen

class EditProfileAdminForm(FlaskForm):
    email = StringField()