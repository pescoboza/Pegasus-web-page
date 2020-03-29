# NOTE: DO NOT format this file bebause it creates
# a circular dependency problem with views.py.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
# TODO: Remove this import from final version and add heroku hostname.
from get_local_host import get_local_host

# ---------------------------------------------------
# Configuration setup
# ---------------------------------------------------
app = Flask(__name__)
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ #
#   TODO: SOLVE EMAIL MANIA ONCE AND FOR ALL!!!   #
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ #
app.config["DEBUG"] = True
app.config["TESTING"] = False
app.config["SECRET_KEY"] = "pegasus-dev-team"
app.config["SECURITY_PASSWORD_SALT"] = "Den Minecraft ist kaputt!"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = get_local_host()
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_SUPPRESS_SEND"] = False
app.config["MAIL_ASCII_ATTACHMENTS"] = True
app.config["MAIL_USERNAME"] = "pegasus.csn@gmail.com"
app.config["MAIL_DEFAULT_SENDER"] = "pegasus.csn@gmail.com"
app.config["MAIL_PASSWORD"] = "std::cout<<\"HelloWorld!\"<<std::endl;"

mail = Mail(app)

db = SQLAlchemy(app)

# ---------------------------------------------------
# Main function
# ---------------------------------------------------
from .models.user import User
from .views import *

db.create_all()

# TODO: Remove this mock admin account
from datetime import datetime
import sys
me = User("Administrator","Developer","lolo23jhon@gmail.com", "lolo23jhon","lolo23jhon",datetime.now())
me.admin = True
me.confirmed = True
me.confirmed_on = datetime.now()
if db.session.query(User).filter(User.username == "lolo23jhon").first() == None:
    db.session.add(me)
    db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)

# # -----------------------------------------------------
# #                    EMAIL TESTING
# # -----------------------------------------------------
# from flask import Flask
# from flask_mail import Mail, Message

# app = Flask(__name__)

# #mail=Mail(app)

# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'pegasus.csn@gmail.com'
# app.config['MAIL_PASSWORD'] = 'std::cout<<"HelloWorld!"<<std::endl;'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_DEFAULT_SENDER'] = 'pegasus.csn@gmail.com'
# app.config['MAIL_ASCII_ATTACHMENTS'] = True
# app.config['DEBUG'] = True

# mail = Mail(app)

# @app.route("/send")
# def index():
#     try:
#         msg = Message('Subject', recipients = ["lolorotmg@gmail.com"])
#         msg.body = "Hello Flask message sent from Flask-Mail"
#         msg.html = "<b>Javivi, si estas viendo esto es porque descrubrí como usar la tenología de nuestros ancestros para mandar correos con una pagina web. Solo para confirmar mandame una imagen de un delfín por whatsapp.</b>"
#         mail.send(msg)
#     except Exception as e:
#         raise e
#     return "Check Your Inbox !!!"

# if __name__ == '__main__':
#     app.run(debug = True)
