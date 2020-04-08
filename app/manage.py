from datetime import datetime
from . import app, db
from .models.user import User

@admin_required
# Creatse an administrator user
def create_admin(first_name, last_name,email, username ,password):
    admin_user = User(first_name, last_name,email, username, password, datetime.utcnow())

    admin_user.confirmed = True
    admin_user.admin = True

    db.session.add(admin_user)
    db.commit()
    token = generate_confirmation_token(admin_user.email)