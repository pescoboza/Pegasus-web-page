from forms import FIELD_LENGTHS as flen


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary=True)
    firstName = db.Columm(db.String(flen["firstName"]["max"]))
    lastName = db.Columm(db.String(flen["lastName"]["max"]))
    email = db.Column(db.String(flen["email"]["max"]), unique=True)
    username = db.Column(db.String(flen["username"]["max"]), unique=True)
    password = db.Column(db.String(flen["password"]["max"]))


    def __init__(self, t_firstName, t_lastName, t_email, t_username, t_password ):
        self.firstName = t_firstName
        self.lastName = t_lastName
        self.email = t_email
        self.username = t_username
        self.password = t_password


# email regex: 	^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$