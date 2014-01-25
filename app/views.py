from flask import render_template
from app import app

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

