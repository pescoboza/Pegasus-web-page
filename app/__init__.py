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
from .models.user import AnonymousUser, User, Role, Permission
from .models.post import Post
from .models.follow import Follow
from .models.comment import Comment
from .views import *
from .views.error_handle import *
from .views.request_password_change import *
from .views.login import *
from .views.logout import *
from .views.chatbot import *
from .views.blog import *
from .views.edit_profile import *
from .views.edit_profile_admin import *
from .views.register import *
from .views.post import *
from .views.edit import *
from .views.follow import *
from .views.followers import *
from .views.followed_by import *
from .views.moderate import *

app.jinja_env.globals.update(Permission=Permission)

def create_tables():
    args = {"bind": db.session.bind, "checkfirst": True}

    Role.__table__.create(**args)
    Role.insert_roles()
    
    User.__table__.create(**args)

    Post.__table__.create(**args)

    Follow.__table__.create(**args)

    Comment.__table__.create(**args)


create_tables()

if __name__ == "__main__":
    app.run()