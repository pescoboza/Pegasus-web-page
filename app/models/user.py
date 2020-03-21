from app import db
from . import FIELD_LENGTHS as flen

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(flen["first_name"]["max"]))
    last_name = db.Column(db.String(flen["last_name"]["max"]))
    email = db.Column(db.String(flen["email"]["max"]), unique=True)
    username = db.Column(db.String(flen["username"]["max"]), unique=True)
    password = db.Column(db.String(flen["password"]["max"]))
    date_created = db.Column(db.DateTime)


    def __init__(self, first_name, last_name, email, username, password, date_created):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.date_created = date_created