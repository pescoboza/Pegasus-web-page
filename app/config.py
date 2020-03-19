from get_localhost import get_localhost

DEBUG = True
SECRET_KEY = "pegasus-dev-team"  # TODO: Add safer secret key.
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = ""  # TODO: Add heroku uri.
if DEBUG:
    SQLALCHEMY_DATABASE_URI = get_localhost()
