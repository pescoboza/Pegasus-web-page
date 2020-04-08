from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Length
from ..validators import NEW_FIELDS as nf

class EditProfileForm(FlaskForm): 
    first_name = nf["first_name"]
    last_name = nf["last_name"]
    location = nf["locatoin"]
    about_me = nf["about_me"]
    
    submit = SubmitField("Submit")