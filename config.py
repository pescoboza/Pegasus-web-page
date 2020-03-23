from get_local_host import get_local_host

class Config:

    # General config
    FLASK_ENV = "development"
    TESTING = True
    DEBUG = True
    SECRET_KEY = "pegasus-dev-team"  # TODO: Add safer secret key.
    
    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # TODO: Change database URI to Heroku database.
    SQLALCHEMY_DATABASE_URI = get_local_host()