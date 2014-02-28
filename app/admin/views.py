from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask.ext.mail import Message, Mail
import traceback

from app.users.models import User
from models import Matching

admin = Blueprint('admin', __name__)

@admin.route('/matching/', methods=('GET', 'POST'))
def admin_index():
	return render_template('admin/matching.html')

@admin.route('/matching/go', methods=('GET', 'POST'))
def admin_math_go():
	ps = User.query.filter(User.status == "p", User.matchable == True).all()
	iis = User.query.filter(User.status == "i", User.matchable == True).all()

	return render_template('admin/matching.html')

@admin.route('/matching/send', methods=('GET', 'POST'))
def admin_math_send():
		matchings = Matching.query.filter(Matching.email_send == False).limit(5)

		
		return "Success!"


