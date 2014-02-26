from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail

from mails import mail
from config import *
from users import views

app = Flask(__name__)
app.config.from_object(__name__)

mail = Mail(app)

from data import db
db = SQLAlchemy(app)

app.register_blueprint(users.views.users)

import views
