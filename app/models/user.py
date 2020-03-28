from passlib.hash import sha256_crypt
from app import db
from . import FIELD_LENGTHS as flen

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(flen["first_name"]["max"]))
    last_name = db.Column(db.String(flen["last_name"]["max"]))
    email = db.Column(db.String(flen["email"]["max"]), unique=True)
    username = db.Column(db.String(flen["username"]["max"]), unique=True)
    password = db.Column(db.String())
    created_on = db.Column(db.DateTime)
    admin = db.Column(db.Boolean, default=False)
    confirmed = db.Column(db.Boolean, default=False)
    confirmed_on = db.Column(db.DateTime)


    def __init__(self, first_name, last_name, email, username, password, created_on):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = sha256_crypt.hash(password)
        self.created_on = created_on
        self.confirmed = False
        self.confirmed_on = None

    # TODO: Implement check for authentication
    def is_authenthicated():
        raise Exception("WRITE ME!")