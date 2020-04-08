from .. import db
from .user import User

class Permission:
    FOLLOW = 1 
    COMMENT = 2
    WRITE = 4
    MODERATE = 8
    ADMIN = 16

ROLES = {
    "user": {
        "permissions": [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE],
        "description": "Basic permissions to write articles and comments and to follow othre users. This is the deault for new users."
    },
    "moderator": {
        "permissions": [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE, Permission.MODERATE],
        "description": "Adds permission to moderate comments made by other users."
    },
    "administrator":{
        "permissions": [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE, Permission.MODERATE, Permission.ADMIN],
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
        if self.permission is None:
            self.permission = 0

    def has_persmission(self, perm):
        return self.permissions & perm == perm

    def add_persmission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_persmission(perm)
            self.permissions -= perm
    
    def reset_permissions(self):
        self.permissions = 0

    @staticmethod
    def insert_roles():
        default_role = "user"
        for r in ROLE:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.reset_permissions()
            for perm in roles[r]["permissions"]:
                role.add_persmission(perm)
            role.default = (role.name == default_role)
            db.session.add(role)
        db.session.commit()
