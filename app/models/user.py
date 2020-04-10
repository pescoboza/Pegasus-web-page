from datetime import datetime
from flask import request
from flask_login import UserMixin, AnonymousUserMixin
from passlib.hash import sha256_crypt, ldap_hex_md5
from .. import app, db, login
from ..validators import FIELD_LENGTHS as flen
from .post import Post


class Permission:
    FOLLOW = 1 
    COMMENT = 2
    WRITE = 4
    WRITE_ARTICLES = 8
    MODERATE = 16
    ADMIN = 32

ROLES = {
    "user": {
        "permissions": [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE_ARTICLES],
        "description": "Basic permissions to write articles and comments and to follow othre users. This is the deault for new users."
    },
    "moderator": {
        "permissions": [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE_ARTICLES, Permission.MODERATE],
        "description": "Adds permission to moderate comments made by other users."
    },
    "administrator":{
        "permissions": [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE_ARTICLES, Permission.MODERATE, Permission.ADMIN],
        "description": "Full access, which includes permission to change the role of other users."
    }
}


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship("User", backref="role", lazy="dynamic")

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:
            self.permission = 0

    def has_permission(self, perm):
        return self.permissions & perm == perm

    def add_persmission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_persmission(perm):
            self.permissions -= perm
    
    def reset_permissions(self):
        self.permissions = 0

    @staticmethod
    def insert_roles():
        default_role = "user"
        for r in ROLES:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.reset_permissions()
            for perm in ROLES[r]["permissions"]:
                role.add_persmission(perm)
            role.default = (role.name == default_role)
            db.session.add(role)
        db.session.commit()


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
    about_me = db.Column(db.String(64))
    location = db.Column(db.String(64))
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow())

    password = db.Column(db.String())

    newsletter = db.Column(db.Boolean, default=False)

    is_authenticated = db.Column(db.Boolean, default=False)
    authenticated_on = db.Column(db.DateTime)
    registered_on = db.Column(db.DateTime)
    
    is_administrator = db.Column(db.Boolean, default=False)


    avatar_hash = db.Column(db.String(32))

    posts = db.relationship("Post", backref="author", lazy="dynamic")
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))


    def check_password(self, password):
        return sha256_crypt.verify(password, self.password)

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)
        db.session.commit()

    def can(self, perm):
        return self.role is not None and self.role.has_permission(perm)

    def is_administrator(self):
        return self.can(Permission.ADMIN)

    def gravatar_hash(self):
        return ldap_hex_md5.hash(self.email)[5:]

    def gravatar(self, size=100, default="identicon", rating="g"):
        url = "https://secure.gravatar.com/avatar" if request.is_secure() else "https://secure.gravatar.com/avatar"
        hash = self.avatar_hash if self.avatar_hash != None else self.gravatar_hash()
        return "{url}/{hash}?s={size}&d={default}&r={rating}".format(url=url, hash=hash, size=size, default=default, rating=rating)

    
    def __init__(self, first_name, last_name, email, username, password, registered_on, newsletter=False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = sha256_crypt.hash(password)
        self.registered_on = registered_on
        self.is_authenticated = False
        self.authenticated_on = None
        self.newsletter = newsletter
        self.avatar_hash = None
        self.role = None

        if self.email == app.config["APP_ADMIN"]:
            self.role = Role.query.filter_by(name="administrator").first()
        if self.role == None:
            self.role = Role.query.filter_by(default=True).first()

        if self.email != None and self.avatar_hash == None:
            self.avatar_hash = self.gravatar_hash()

class AnonymousUser(AnonymousUserMixin):
    def can(self, perm):
        return False

    def is_administrator(self):
        return False 