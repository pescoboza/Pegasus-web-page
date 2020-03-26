from datetime import datetime
from passlib.hash import sha256_crypt
from . import app, db
from .models.user import User

@manager.command
# Creatse an administrator user
def create_admin(first_name, last_name,email, username ,password):
    admin_user = User(first_name, last_name,email, username, sha256_crypt.hash(password), datetime.now().ctime())

    admin_user.confirmed = True
    admin_user.admin = True

    db.session.add(admin_user)
    db.commit()
    token = generate_confirmation_token(admin_user.email)