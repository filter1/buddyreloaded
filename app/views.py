from flask import render_template, request
from app import app
from models import db

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/impress')
def impress():
	return 'll'

@app.route('/privacy')
def about_us():
	return 'privacy'

@app.route('/contact')
def contac():
	return 'contac '

@app.route('/admin')
def admin():
	return 'Admin'

@app.route('/activate/<token>')
def activate(token):
	return 'Token is %s' %token

@app.route('/register', methods = ['POST'])
def register():
	return request.form['name']

@app.route('/testdb')
def testdb():
  if db.session.query("1").from_statement("SELECT 1").all():
    return 'It works.'
  else:
    return 'Something is broken.'