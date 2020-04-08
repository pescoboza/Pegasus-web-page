from flask_login import UserMixin
from passlib.hash import sha256_crypt
from app import db, login
from . import FIELD_LENGTHS as flen
from .post import Post


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin,db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(flen["first_name"]["max"]))
    last_name = db.Column(db.String(flen["last_name"]["max"]))
    email = db.Column(db.String(flen["email"]["max"]), unique=True)
    username = db.Column(db.String(flen["username"]["max"]), unique=True)
    password = db.Column(db.String())
    registered_on = db.Column(db.DateTime)
    is_administrator = db.Column(db.Boolean, default=False)
    confirmed = db.Column(db.Boolean, default=False)
    confirmed_on = db.Column(db.DateTime)
    newsletter = db.Column(db.Boolean)

    about_me = db.Column(db.String(64))
    location = db.Column(db.String(64))
    last_seen = db.Column(db.Datetime(), default=datetime.utcnow())

    posts = db.relationship("Post", backref="author", lazy="dynamic")


    def __init__(self, first_name, last_name, email, username, password, registered_on, newsletter=False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = sha256_crypt.hash(password)
        self.registered_on = registered_on
        self.confirmed = False
        self.confirmed_on = None
        self.newsletter = newsletter

    def check_password(self, password):
        return sha256_crypt.verify(password, self.password)

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)
        db.session.commit()