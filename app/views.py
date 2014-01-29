from flask import render_template, request, flash, redirect, Markup, session
from app import app
from models import db, User
from mails import send_token
from lang import lang_array

@app.route('/')
@app.route('/index.html')
def index():
	if 'uid' not in session:
		return render_template('index_reg.html', lang=lang_array)

	uid = session['uid']
	user = User.query.get(uid)
	return render_template('index_intern.html', user=user)

@app.route('/impress.html')
def impress():
	return render_template('impress.html')

@app.route('/privacy.html')
def about_us():
	return render_template('privacy.html')

@app.route('/contact.html')
def contac():
	return render_template('contact.html')

@app.route('/admin')
def admin():
	return 'Admin'

@app.route('/token/<token_str>')
def token(token_str):
	user = User.query.filter_by(token = token_str).first()

	if user == None:
		message = Markup('Something with the token went wrong.')
		return redirect('/')
	else:
		user.token = None
		db.session.commit()
		session['uid'] = user.uid #login
		message = Markup('Successfully activated the account.')

	flash(message)
	return redirect('/')

@app.route('/register', methods = ['POST'])
def register():
	new_user = User(** (request.form.to_dict(flat=True))) # converting to normal dict


	try:
		db.session.add(new_user)
		db.session.commit()

		send_token(new_user.name, new_user.email, new_user.token)
	except Exception, e:
		message = Markup("Something went wrong. Please try again:" + str(e))
		flash(message)
		return redirect('/')

	message = Markup("You successfully registred. Now check your emails and activate the account!")
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
				if user.token == None: # check if activated
					session['uid'] = user.uid
					message = Markup('You successfully logged in.')
				else:
					message = Markup('Please activate your account and vist the link which we send to your email. Also check your Junk Folder.')
			else:
				message = Markup('Your password is incorrect.')
		else:
			message = Markup('We did not find your email adress.')
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
