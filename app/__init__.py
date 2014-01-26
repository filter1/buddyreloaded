from flask import Flask

app = Flask(__name__)
from app import views

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:lollol@localhost/development'
app.secret_key = 'why would I tell you my secret key?'

from models import db
db.init_app(app)