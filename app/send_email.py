from . import app

def get_src_from_file(filename):
    src = str()
    with open(filename, 'r') as f:
        src = f.read()
    if not src:
        raise EmptyFile("The file {} was empty!".format(filename))
    return src

def 

import smtplib
from email.mime.text import MIMEText

# TODO: Setup email sending.
def send_email(receiver_email,message, subject):
    msg = MIMEText(message, "html")
    msg["Subject"] = subject
    msg["From"] = app.config["MAIL_USERNAME"]
    msg["To"] = receiver_email

    #Send the email
    with smtplib.SMTP(smltp_server,port) as server:
        server.login(app.config["MAIL_USERNAME"], app.config["MAIL_PASSWORD"])
        server.sendmail(app.config["MAIL_USERNAME"], receiver_email, msg.as_string())


def send_emails()(message, port, smltp_server, login, password, sender_email, receiver_emails, subject):
    msg = MIMEText(message, "html")
    msg["Subject"] = subject
    msg["From"] = sender_email

    server.login(login, password)
    
    with smtplib.SMTP(smltp_server,port) as server:
        for receiver_email in receiver_emails:
            msg["To"] = receiver_email
            server.sendmail(sender_email, receiver_email, msg.as_string())
