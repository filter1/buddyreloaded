from flask import render_template, request, flash, redirect, Markup, session, Blueprint

from app.mails import send_token, send_notification
from lang import lang_array

from app.users.models import User
from app.data import db

users = Blueprint('users', __name__)

@users.route('/token/<token_str>')
def token(token_str):
	user = User.query.filter_by(token = token_str).first()

	if user == None:
		message = Markup('Something with the token went wrong.')
		return redirect('/')
	else:
		user.token = None
		db.session.commit()
		session['uid'] = user.id #login
		message = Markup('Successfully activated the account.')

	flash(message)
	return redirect('/')


@users.route('/register', methods = ['POST'])
def register():
	new_user = User(** (request.form.to_dict(flat=True))) # converting to normal dict
	try:
		db.session.add(new_user)
		db.session.commit()

		send_token(new_user.name, new_user.email, new_user.token)
	except Exception, e:
		message = Markup("Something went wrong. It looks like the Email Address is aleady in use.") + str(e)
		flash(message)
		return redirect('/')
	send_notification(new_user.email) # sending Email to contact@buddy-md.de
	message = Markup("Please activate your Email Address.")
	flash(message)
	return redirect('/')


@users.route('/login', methods = ['POST'])
def login():
	user = User.query.filter_by(email = request.form['email']).first()
	if user != None:
		if user.check_password(request.form['password']):
			if user.token == None: # check if activated
				session['uid'] = user.id
				message = Markup('You successfully logged in.')
			else:
				message = Markup('Please activate your account and vist the link which we send to your email. Also check your Junk Folder.' + user.token)
		else:
			message = Markup('Your password is incorrect.')
	else:
		message = Markup('We did not find your email adress.')
	flash(message)

	if user != None and user.is_admin():
		return redirect('/admin')

	return redirect('/')


@users.route('/logout', methods = ['GET', 'POST'])
def logout():
	session.pop('uid', None)
	return redirect('/')

