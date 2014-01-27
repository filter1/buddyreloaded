import os

# email server
MAIL_SERVER = 'triangulum.uberspace.de'
MAIL_PORT = 587
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('EMAIL_USER')
MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

from flask import Flask
from flask.ext.mail import Mail

app = Flask(__name__)
app.config.from_object(__name__)
mail = Mail(app)

#config
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://buddies:NabnuvwazsuorvAnErc2@localhost/buddies_buddy'
app.secret_key = 'why would I tell you my secret key?'

from models import db
db.init_app(app)


from app import views
