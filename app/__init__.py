

from flask import Flask

app = Flask(__name__)
from app import views

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mysql:lollol@localhost:3306/development'
from models import db
db.init_app(app)