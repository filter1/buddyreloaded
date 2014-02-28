from flask import Blueprint, redirect, render_template, request

from app.users.models import User
from models import Matching
from helper import send_matching_email, calculate_score
from app.data import db

admin = Blueprint('admin', __name__)

@admin.route('/admin/', methods=('GET', 'POST'))
def admin_index():
	return render_template('admin/index.html')


@admin.route('/admin/match_all', methods=('GET', 'POST'))
def admin_match_all():
	ps_all = User.query.filter(User.status == "p", User.matchable == True).order_by(User.registration_date).all()

	for ps in ps_all:
		iis_all = User.query.filter(User.status == "i", User.matchable == True).all()
		best_score = None
		best_match = None

		for iis in iis_all:
			score = calculate_score(ps, iis)
			if not best_score or score > best_score:
				best_score = score
				best_match = iis

		if best_score:
			m = Matching(ps.id, best_match.id)
			db.session.add(m)
			ps.matchable = False
			best_match.matchable = False
			db.session.commit()

	return "Sucess!"


@admin.route('/admin/match_two/', methods=('GET','POST'))
def admin_match_two():
	ps_id = int(request.form['ps'])
	iis_id = int(request.form['iis'])
	ps = User.query.get(ps_id)
	iis = User.query.get(iis_id)
	m = Matching(ps.id, iis.id)
	ps.matchable = False
	iis.matchable = False
	db.session.add(m)
	db.session.commit()
	return "Success!"


@admin.route('/admin/matching_send_emails', methods=('GET','POST'))
def admin_match_send():
		matchings = Matching.query.filter(Matching.email_send == False).limit(5)
		send_matching_email(matchings)
		return "Success!"

@admin.route('/admin/matching_show_all', methods=('GET','POST'))
def admin_match_show_all():
		matchings = Matching.query.join(User).all()
		return render_template('admin/matching_show_all.html', matchings=matchings)


