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
    return '<Matching %r>' % (self.id)

  def to_table(self):
    res = "<tr> <td>%s</td> <td>%s</td> <td>%s</td> %s %s </tr>" %(self.id, self.matched_on, self.email_send, self.ps.to_table(), self.iis.to_table())
    return res

  def to_matching_short_table(self):
    res = "<tr> <td>%s</td> <td>%s</td> <td>%s</td> %s %s </tr>" %(self.id, self.matched_on, self.email_send, self.ps.to_short_table(), self.iis.to_short_table())
    return res