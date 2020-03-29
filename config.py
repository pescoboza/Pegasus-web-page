from get_local_host import get_local_host

class Config:

    # General config
    ENV = "development"
    TESTING = True
    DEBUG = True
    SECRET_KEY = "pegasus-dev-team"  # TODO: Add safer secret key.
    # TODO: Add security password salt
    SECURITY_PASSWORD_SALT = '\0'
    
    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # TODO: Change database URI to Heroku database.
    SQLALCHEMY_DATABASE_URI = get_local_host()

    # Email settings
    MAIL_SERVER = "smpt.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = "pegasus.csn@gmail.com"
    MAIL_PASSWORD = "std::cout<<\"HelloWorld!\"<<std::endl;"
    MAIL_SUPPRESS_SEND = False
