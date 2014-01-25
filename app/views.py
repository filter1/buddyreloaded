from app import app

@app.route('/')
def index():
  return 'Index'

@app.route('/impress')
def impress():
	return 'impress'

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

