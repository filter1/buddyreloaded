from flask.ext.mail import Message
from app import mail
from flask import render_template

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender = sender, recipients = recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

def send_token(name, email, token):
    send_email("[BUDDY-MD] Registration",
        "noreply@budd-md.de",
        [email],
        render_template("email_token.txt", 
            name = name, token = token, url = 'http://www.buddy-md.de/token/' + str(token)),
        render_template("email_token.html", 
            name = name, token = token, url = 'http://www.buddy-md.de/token/' + str(token)))