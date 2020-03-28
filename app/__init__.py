# NOTE: DO NOT format this file bebause it creates
# a circular dependency problem with views.py.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

# ---------------------------------------------------
# Configuration setup
# ---------------------------------------------------
app = Flask(__name__)
app.config.from_object("config.Config")

db = SQLAlchemy(app)

mail = Mail(app)


# ---------------------------------------------------
# Main function
# ---------------------------------------------------
from .models.user import User
from .views import *

db.create_all()

# TODO: Remove this mock admin account
from datetime import datetime
me = User("Administrator","Developer","lolo23jhon@gmail.com", "lolo23jhon","lolo23jhon",datetime.now())
me.admin = True
me.confirmed = True
me.confirmed_on = datetime.now()
if db.session.query(User).filter(User.username == "lolo23jhon").first() == None:
    db.session.add(me)
    db.session.commit()


if __name__ == "__main__":
    app.run()    