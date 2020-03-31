from threading import Thread
from flask import render_template
from flask_mail import Mail, Message
from . import app, mail


def send_async_email(msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, recipients, text_body=None, html_body=None, cc=None, bcc=None):
    msg = Message(
        subject=subject,
        sender=app.config["MAIL_DEFAULT_SENDER"],
        recipients=recipients,
        cc=cc,
        bcc=bcc,
        body=text_body,
        html=html_body
    )
    thr = Thread(target=send_async_email, args=[msg])
    thr.start()
