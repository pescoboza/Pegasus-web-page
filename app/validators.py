from wtforms import StringField, PasswordField
from wtforms.validators import Email, Length, DataRequired, Regexp

# validators.py contains all the fields reused over different components of the web application.


FIELD_LENGTHS = {
    "username": {
        "min": 8,
        "max": 16,
        "message": None
    },
    "password": {
        "min": 8,
        "max": 30,
        "message": None
    },
    "first_name": {
        "min": 1,
        "max": 30,
        "message": None
    },
    "last_name": {
        "min": 1,
        "max": 30,
        "message": None
    },
    "email": {
        "min": 5,
        "max": 254,
        "message": None
    },
    "location": {
        "min": 0,
        "max": 64,
        "message": None
    },
    "about_me": {
        "min": 0,
        "max": 64,
        "message": None
    }
}


NEW_FIELDS = {
    "username": StringField(label="Username",
                            validators=[InputRequired(),
                                        Length(**FIELD_LENGTHS["username"]),
                                        Regexp("^[A-Za-z][A-Za-Z0-9_.]*$", 0,
                                               "Usernames must only contain letters, numbers, dots ('.') or underscores ('_').")]),

    "email": StringField(label="Email",  validators=[
        DataRequired(), Length(**FIELD_LENGTHS["email"]), Email()]),

    "first_name": StringField(label="First Name", validators=[
        DataRequired(), Length(**FIELD_LENGTHS["first_name"])]),

    "last_name": StringField(label="Last Name", validators=[
        DataRequired(), Length(**FIELD_LENGTHS["last_name"])]),

    "password": PasswordField(label="Password", validators=[
        DataRequired(),
        Length(**FIELD_LENGTHS["password"])]),

    "location": StringField("Location", validators=[Length(**FIELD_LENGTHS["location"])]),
    
    "about_me": StringField("About me", validators=[Length(**FIELD_LENGTHS["about_me"])])
}
