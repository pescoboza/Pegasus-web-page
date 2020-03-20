from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary=True)
    name = db.Columm(db.String(60))
    lastname = db.Columm(db.String(60))
    email = db.Column(db.String(60))
    username = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(60))

    @staticmethod
    # Returns the total number of users in the database.
    def num_users():

# email regex: 	^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$