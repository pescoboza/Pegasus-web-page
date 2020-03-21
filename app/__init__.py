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
me = User("Administrator","Developer","lolo23jhon@gmail.com", "lolo23jhon","lolo23jhon")
db.session.add(me)
db.session.commit()
if __name__ == "__main__":

    app.run()