import os

# email server
MAIL_SERVER = 'smtp.triangulum.uberspace.de'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False

#MAIL_USERNAME = os.environ.get('EMAIL_USER')
#MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
MAIL_USERNAME = 'buddies'
MAIL_PASSWORD = 'Geyb-Dab-jUd-tAm-foo'

from flask import Flask
from flask.ext.mail import Mail

app = Flask(__name__)
app.config.from_object(__name__)
mail = Mail(app)

#config
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://buddies:NabnuvwazsuorvAnErc2@localhost/buddies_buddy'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:lollol@localhost/development'


app.secret_key = 'why would I tell you my secret key?'




from models import db
db.init_app(app)


from app import views
