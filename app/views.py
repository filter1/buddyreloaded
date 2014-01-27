from flask import render_template, request, flash, redirect, Markup, session
from app import app
from models import db, User

@app.route('/')
@app.route('/index.html')
def index():
	if 'uid' not in session:
		return render_template('index_reg.html')

	uid = session['uid']
	user = User.query.get(uid)
	return render_template('index_intern.html', user=user)

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
	new_user = User(** (request.form.to_dict(flat=True))) # converting to normal dict

	# trying
	try:
		db.session.add(new_user)
		db.session.commit()
	except:
		message = Markup("Something went wrong. Please try again.")
		flash(message)
		return redirect('/')
	message = Markup("You successfully registerd!")
	flash(message)
	return redirect('/')

@app.route('/testdb')
def testdb():
  if db.session.query("1").from_statement("SELECT 1").all():
    return 'It works.'
  else:
    return 'Something is broken.'

@app.route('/login', methods = ['POST'])
def login():
	try:
		user = User.query.filter_by(email = request.form['email']).first()

		if user != None:
			if user.check_password(request.form['password']):
				session['uid'] = user.uid
				message = Markup('You successfully logged it')
			else:
				message = Markup('Your password is incorrect.')
		else:
			message = Markup('We did not find your email.')
	except Exception, e:
		message = str(e)
	flash(message)
	return redirect('/')

@app.route('/logout', methods = ['GET', 'POST'])
def logout():
	session.pop('uid', None)
	return redirect('/')

@app.route('/change_matchable', methods = ['POST'])
def change_matchable():
	if 'uid' not in session:
		return redirect('/')

	uid = session['uid']
	user = User.query.get(uid)
	user.matchable = not user.matchable
	db.session.commit()
	return redirect('/')
