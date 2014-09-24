from flask import Blueprint, redirect, render_template, request, session
import time

from app.users.models import User
from models import Matching
from helper import send_matching_email, calculate_score
from app.data import db

admin = Blueprint('admin', __name__)

@admin.before_request
def restrict_to_admins():
	if 'uid' not in session:
		return redirect('/')
	id = session['uid']
	user = User.query.get(id)

	if not user.is_admin():
		return redirect('/')


@admin.route('/admin/', methods=('GET', 'POST'))
@admin.route('/admin/control', methods=('GET', 'POST'))
def admin_control():
	open_ps = User.query.filter(User.status == 'p', User.matchable == True).count()
	num_ps = User.query.filter(User.status == 'p').count()
	open_iis = User.query.filter(User.status == 'i', User.matchable == True).count()
	num_iis = User.query.filter(User.status == 'i').count()
	num_matchings = Matching.query.count()
	open_mails = Matching.query.filter(Matching.email_send == False).count()

	ps = User.query.filter(User.status == 'p', User.matchable == True).all()
	iis = User.query.filter(User.status == 'i', User.matchable == True).all()

	return render_template('admin/control.html', open_ps=open_ps, num_ps=num_ps,
		open_iis=open_iis, num_iis=num_iis, num_matchings=num_matchings, open_mails=open_mails,
		ps=ps, iis=iis)


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
	matchings = Matching.query.filter(Matching.email_send == False).limit(3)
	for m in matchings:
		send_matching_email(m)
		time.sleep(3)
	return "Success!"

@admin.route('/admin/set_ps_matchable_if_not_max_buddies', methods=('GET','POST'))
def admin_set_ps_matchable_if_not_max_buddies():
	users = User.query.filter(User.status == "p").all()
	for u in users:
		m = Matching.query.filter(Matching.ps_id == u.id).all()
		if m.length < u.max_buddies:
			u.matchable = True
	return "Success!"


@admin.route('/admin/pairs_all', methods=('GET','POST'))
def admin_match_show_all():
		matchings = Matching.query.all()

		return render_template('admin/matching_show_all.html', matchings=matchings)


@admin.route('/admin/pairs', methods=('GET','POST'))
def admin_matching_short():
		matchings = Matching.query.all()

		return render_template('admin/matching_short.html', matchings=matchings)


@admin.route('/admin/registrations', methods=('GET','POST'))
def admin_reg_all():
		users = User.query.all()
		emails = ''
		for u in users:
			emails += u.email + '; '

		return render_template('admin/registrations.html', users=users, emails=emails)


@admin.route('/admin/registrations_open_iis', methods=('GET','POST'))
def admin_reg_open_iis():
		users = User.query.filter(User.status == 'i', User.matchable == True).all()
		emails = ''
		for u in users:
			emails += u.email + '; '

		return render_template('admin/registrations.html', users=users, emails=emails)


@admin.route('/admin/registrations_open_ps', methods=('GET','POST'))
def admin_reg_open_ps():
		users = User.query.filter(User.status == 'p', User.matchable == True).all()
		emails = ''
		for u in users:
			emails += u.email + '; '
			
		return render_template('admin/registrations.html', users=users, emails=emails)

@admin.route('/admin/search', methods=('GET', 'POST'))
def admin_search():
	return render_template('admin/search.html')