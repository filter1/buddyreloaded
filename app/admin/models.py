from flask.ext.sqlalchemy import SQLAlchemy

from app.data import db
from app.users.models import User

class Matching(db.Model):
  __tablename__ = 'matchings'
  id = db.Column(db.Integer, primary_key=True)

  ps_id = db.Column(db.Integer, db.ForeignKey(User.id))
  iis_id = db.Column(db.Integer, db.ForeignKey(User.id))

  email_send = db.Column(db.Boolean, default=False)
  matched_on = db.Column(db.DateTime, default=db.func.now())

  ps = db.relationship('User', foreign_keys='Matching.ps_id')
  iis = db.relationship('User', foreign_keys='Matching.iis_id')

  def __init__(self, ps_id, iis_id):
    self.ps_id = ps_id
    self.iis_id = iis_id

  def __repr__(self):
    return '<Matching %r,%r,%r>' % self.id, self.ps_id, self.iis_id