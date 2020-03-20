from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary=True)
    name = db.Columm(db.String(16))
    lastname = db.Columm(db.String(16))
    email = db.Column(db.String(64))
    username = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(32))

# email regex: 	^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$