from flask import Flask

app = Flask(__name__)
from app import views


#config
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:lollol@localhost/development'
app.secret_key = 'why would I tell you my secret key?'

# email server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'johannes.filter'
MAIL_PASSWORD = 'dert2012'


app.config.from_object(__name__)

from flask.ext.mail import Mail

mail = Mail(app)

from models import db
db.init_app(app)