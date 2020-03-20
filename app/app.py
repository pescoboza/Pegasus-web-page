# NOTE: DO NOT format this file bebause it creates
# a circular dependency problem with views.py.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

# ---------------------------------------------------
# Configuration setup
# ---------------------------------------------------
app = Flask(__name__)


app.debug = config.DEBUG
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config["SECRET_KEY"] = config.SECRET_KEY

db = SQLAlchemy(app)

# ---------------------------------------------------
# Main function
# ---------------------------------------------------
from views import *

if __name__ == "__main__":
    app.run()