from app import db
from forms import FIELD_LENGTHS as flen


class User(db.Model):
    id = db.Column(db.Integer, primary=True)
    firstName = db.Columm(db.String(flen["firstName"]["max"]))
    lastName = db.Columm(db.String(flen["lastName"]["max"]))
    email = db.Column(db.String(flen["email"]["max"]), unique=True)
    username = db.Column(db.String(flen["username"]["max"]), unique=True)
    password = db.Column(db.String(flen["password"]["max"]))

    __tablename__ = "users"

    def __init__(self, t_firstname, t_lastname )

    @staticmethod
    # Returns the total number of users in the database.
    def num_users():

# email regex: 	^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$