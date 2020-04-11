# NOTE: DO NOT format this file bebause it creates
# a circular dependency problem with views.py.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
# TODO: Remove this import from final version and add heroku hostname.
from get_local_host import get_local_host

# ---------------------------------------------------
# Configuration setup
# ---------------------------------------------------
app = Flask(__name__)
app.config.from_object("config.Config")

login = LoginManager(app)
login.login_view = "login"
mail = Mail(app)
moment = Moment(app)

db = SQLAlchemy(app)

# ---------------------------------------------------
# Main function
# ---------------------------------------------------
from .models.user import User, Role, Permission
from .models.post import Post
from .views import *
from .views.request_password_change import request_password_change
from .views.login import login
from .views.logout import logout
from .views.chatbot import chatbot
from .views.blog import blog
from .views.edit_profile import edit_profile
from .views.edit_profile_admin import edit_profile_admin
from .views.register import register
from .views.post import post
from .views.edit import edit
    

app.jinja_env.globals.update(Permission=Permission)

def create_tables():
    args = {"bind": db.session.bind, "checkfirst": True}

    Role.__table__.create(**args)
    Role.insert_roles()
    
    User.__table__.create(**args)

    Post.__table__.create(**args)

create_tables()

if __name__ == "__main__":
    app.run()

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ #
#        TODO: GET THE BLOG WORKING           #
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ #
# - Figure out the creation order of data tables.
#       - Solve role being of type None in User objects.
#       - This automatically redirects logged in users to the index.