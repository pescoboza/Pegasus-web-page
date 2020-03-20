def get_localhost():
    uri = str()
    with open("db-uri.txt", 'r') as f:
        uri = f.read()
    return uri


DEBUG = True
SECRET_KEY = "pegasus-dev-team"  # TODO: Add safer secret key.
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = ""  # TODO: Add heroku uri.
if DEBUG:
    SQLALCHEMY_DATABASE_URI = get_localhost()
