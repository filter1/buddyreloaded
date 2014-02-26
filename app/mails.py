from flask.ext.mail import Message, Mail
from flask import render_template

mail = Mail()

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender = sender, recipients = recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

def send_token(name, email, token):
    send_email("[BUDDY-MD] Registration",
        "noreply@buddy-md.de",
        [email],
        render_template("email_token.txt", 
            name = name, token = token, url = 'http://buddy-md.de/token/' + str(token)),
        render_template("email_token.html", 
            name = name, token = token, url = 'http://buddy-md.de/token/' + str(token)))

def send_notification(email):
    send_email("[INFO] Registration: %s" % email,
            "noreply@buddy-md.de",
            ["contact@buddy-md.de"],
            "New Registration: %s " % email,
            "New Registration: %s " % email
        )
