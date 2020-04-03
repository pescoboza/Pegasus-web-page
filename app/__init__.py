# NOTE: DO NOT format this file bebause it creates
# a circular dependency problem with views.py.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
# TODO: Remove this import from final version and add heroku hostname.
from get_local_host import get_local_host

# ---------------------------------------------------
# Configuration setup
# ---------------------------------------------------
app = Flask(__name__)
app.config.from_object("config.Config")

mail = Mail(app)

db = SQLAlchemy(app)

# ---------------------------------------------------
# Main function
# ---------------------------------------------------
from .models.user import User
from .views import *
from .views.request_password_change import request_password_change
from .views.logout import logout
db.create_all()

# TODO: Remove this mock admin account
from datetime import datetime
import sys
me = User("Administrator","Developer","lolo23jhon@gmail.com", "lolo23jhon","lolo23jhon",datetime.now())
me.admin = True
me.confirmed = True
me.confirmed_on = datetime.now()
if db.session.query(User).filter(User.username == "lolo23jhon").first() == None:
    db.session.add(me)
    db.session.commit()


if __name__ == "__main__":
    app.run()

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ #
#           TODO: SOLVE MISSING FLASHES           #
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ #