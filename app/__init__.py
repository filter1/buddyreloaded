#config


# email server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'johannes.filter'
MAIL_PASSWORD = ''

from flask import Flask
from flask.ext.mail import Mail

app = Flask(__name__)
app.config.from_object(__name__)
mail = Mail(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:lollol@localhost/development'
app.secret_key = 'why would I tell you my secret key?'

from models import db
db.init_app(app)


from app import views