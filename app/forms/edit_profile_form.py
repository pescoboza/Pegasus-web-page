from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Length
from ..models import FIELD_LENGTHS as flen

class EditProfileForm(FlaskForm): 
    first_name = StringField("Real name"), validators=[Length(**flen["first_name"])])
    last_name = StringField("Real name"), validators=[Length(**flen["last_name"])])
    location = StringField("Location", validators=[Length(**flen["location"])])
    
    submit = SubmitField("Submit")