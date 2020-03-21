
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary=True)
    firstName = db.Columm(db.String(FIELD_LENGTHS["firstName"]["max"]))
    lastName = db.Columm(db.String(FIELD_LENGTHS["lastName"]["max"]))
    email = db.Column(db.String(FIELD_LENGTHS["email"]["max"]), unique=True)
    username = db.Column(db.String(FIELD_LENGTHS["username"]["max"]), unique=True)
    password = db.Column(db.String(FIELD_LENGTHS["password"]["max"]))


    def __init__(self, t_firstName, t_lastName, t_email, t_username, t_password ):
        self.firstName = t_firstName
        self.lastName = t_lastName
        self.email = t_email
        self.username = t_username
        self.password = t_password