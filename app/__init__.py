# NOTE: DO NOT format this file bebause it creates
# a circular dependency problem with views.py.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# ---------------------------------------------------
# Configuration setup
# ---------------------------------------------------
app = Flask(__name__)
app.config.from_object("config.Config")

db = SQLAlchemy(app)


# ---------------------------------------------------
# Main function
# ---------------------------------------------------
from .models.user import User
from .views import *

db.create_all()

# TODO: Remove this mock admin account
from datetime import datetime
from passlib.hash import sha256_crypt
me = User("Administrator","Developer","lolo23jhon@gmail.com", "lolo23jhon",sha256_crypt.hash("lolo23jhon"),datetime.now())
me.admin = True
if db.session.query(User).filter(User.username == "lolo23jhon").first() == None:
    db.session.add(me)
    db.session.commit()

if __name__ == "__main__":
    app.run()