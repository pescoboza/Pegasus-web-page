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


# class User(db.Model):
#     __tablename__ = "user"
#     id = db.Column(db.Integer, primary=True)
#     username = db.Column(db.String(16), unique=True)
#     password = db.Column(db.String(32))
