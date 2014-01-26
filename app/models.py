from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
 
db = SQLAlchemy()
 
class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(100), nullable=False)
  surname = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(100), unique=True, nullable=False)
  password_hash = db.Column(db.String(100), nullable=False)
  dob = db.Column(db.Date, nullable=False)
  gender = db.Column(db.String(1), nullable=False)
  faculty = db.Column(db.String(50), nullable=False)
  lang1 = db.Column(db.String(50))
  lang2 = db.Column(db.String(50))
  lang3 = db.Column(db.String(50))
  remarks = db.Column(db.Text)
  rank = db.Column(db.Integer)
  status = db.Column(db.Integer)
  registration_date = db.Column(db.DateTime)
  last_login = db.Column(db.DateTime)
  num_logins = db.Column(db.Integer)
  token = db.Column(db.String(100))

  def __init__(self, **dict):
    self.name = dict['name'].title
    self.surname = dict['surname'].title
    self.email = dict['email'].lower
    self.set_password(dict['password'])
    self.dob = dict['dob']
    self.gender = dict['gender']
    self.faculty = dict['faculty']
    self.lang1 = dict['lang1'] 
    self.lang2 = dict['lang2']
    self.lang3 = dict['lang3']
    self.remarks = dict['remarks']
     
  def set_password(self, password):
    self.password_hash = generate_password_hash(password)
   
  def check_password(self, password):
    return check_password_hash(self.password_hash, password)