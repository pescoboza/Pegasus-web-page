from datetime import datetime 
from .. import db

class Post(db.Model):
    __tablename__="posts"
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
