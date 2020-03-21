# NOTE: DO NOT format this file bebause it creates
# a circular dependency problem with views.py.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

# ---------------------------------------------------
# Configuration setup
# ---------------------------------------------------
app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

from app.models import User


# ---------------------------------------------------
# Main function
# ---------------------------------------------------
from views import *

if __name__ == "__main__":
    db.create_all()
    app.run()