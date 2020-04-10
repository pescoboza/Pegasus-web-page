# NOTE: DO NOT format this file bebause it creates
# a circular dependency problem with views.py.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
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

db = SQLAlchemy(app)

# ---------------------------------------------------
# Main function
# ---------------------------------------------------
from .models.user import User, Role
from .views import *
from .views.request_password_change import request_password_change
from .views.login import login
from .views.logout import logout
from .views.chatbot import chatbot
from .views.blog import blog
from .views.edit_profile import edit_profile
from .views.edit_profile_admin import edit_profile_admin
from .views.register import register
    

db.create_all()
Role.insert_roles()

if __name__ == "__main__":
    app.run()