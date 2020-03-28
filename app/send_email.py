from threading import Thread
from flask import render_template
from flask_mail import Mail, Message
from . import app, mail
from .decorators import async_

@async_ 
def send_async_email(subject,recipients,text_body,html_body=None,cc=None,bcc=None):
    try:
        msg = Message(
            subject=subject,
            sender=app.config["MAIL_USERNAME"],
            recipients=recipients,
            cc=cc,
            bcc=bcc,
            body=text_body,
            html=html_body 
            )
        return "200"    
    except Exception as e:
        return str(e)



# TODO: set MAX_EMAIL flag in config.py.
def send_email(subject,recipients,text_body=None,html_body=None,cc=None,bcc=None):
    try:
        msg = Message(
            subject=subject,
            sender=app.config["MAIL_USERNAME"],
            recipients=recipients,
            cc=cc,
            bcc=bcc,
            body=text_body,
            html=html_body 
            )
        mail.send(msg)
        return "200"    
    except Exception as e:
        return str(e)