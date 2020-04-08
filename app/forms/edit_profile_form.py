from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Length
from ..validators import create_new_field

class EditProfileForm(FlaskForm): 
    first_name = create_new_field["first_name"]
    last_name = create_new_field["last_name"]
    location = create_new_field["location"]
    about_me = create_new_field["about_me"]
    
    submit = SubmitField("Submit")