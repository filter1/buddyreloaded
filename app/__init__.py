from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail

from mails import mail
from config import *
from users import views
from admin import views

app = Flask(__name__)
app.config.from_object(__name__)

mail = Mail(app)

from data import db
db = SQLAlchemy(app)


from users.models import *
from admin.models import *

# db.drop_all(app=app)
# db.create_all(app=app)

app.register_blueprint(users.views.users)
app.register_blueprint(admin.views.admin)

if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    mail_handler = SMTPHandler('smtp.triangulum.uberspace.de',
                               'server-error@buddy-md.de',
                               ['bugs@buddy-md.de'], 'YourApplication Failed')
    mail_handler.setLevel(logging.ERROR)

    # mail_handler.setFormatter(Formatter('''
    # Message type:       %(levelname)s
    # Location:           %(pathname)s:%(lineno)d
    # Module:             %(module)s
    # Function:           %(funcName)s
    # Time:               %(asctime)s

    # Message:
    
    # %(message)s
    # '''))

    app.logger.addHandler(mail_handler)

import views
