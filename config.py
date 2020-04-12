from get_local_host import get_local_host

class Config:
    DEBUG = True
    TESTING = False
    SECRET_KEY = "pegasus-dev-team"
    SECURITY_PASSWORD_SALT = "Den Minecraft ist kaputt!"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = get_local_host()
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_SUPPRESS_SEND = False
    MAIL_ASCII_ATTACHMENTS = True
    MAIL_USERNAME = "pegasus.csn@gmail.com"
    MAIL_DEFAULT_SENDER = "pegasus.csn@gmail.com"
    MAIL_PASSWORD = "std::cout<<\"HelloWorld!\"<<std::endl;"

    APP_ADMIN = "lolo23jhon@gmail.com"
    APP_POSTS_PER_PAGE = 20
    APP_FOLLOWERS_PER_PAGE = 20
