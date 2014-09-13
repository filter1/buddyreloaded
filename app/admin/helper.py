import traceback
import math

from flask.ext.mail import Message, Mail
from flask import render_template

from app.mails import mail
from app.data import db

def send_matching_email(pair): 
	with mail.connect() as conn:
		try:
			message = render_template("admin/email_to_iis.txt", iis = pair.iis, ps = pair.ps)
			subject = "[Buddy] You have a Buddy!"
			msg = Message(
				recipients=[pair.iis.email],
				bcc=["contact@buddy-md.de"],
				sender="buddy@stura-md.de",
			  body=message,
			  subject=subject)
			conn.send(msg)

			message = render_template("admin/email_to_ps.txt", iis = pair.iis, ps = pair.ps)
			subject = "[Buddy] You have a Buddy!"
			msg = Message(
				recipients=[pair.ps.email],
				bcc=["contact@buddy-md.de"],
				sender="buddy@stura-md.de",
			  body=message,
			  subject=subject)
			conn.send(msg)

			pair.email_send = True
		except Exception, e:
			print "Fail: %s" % e
			traceback.print_exc()
	db.session.commit()

def calculate_score(ps, iis):
	score = 0

	if ps.gender == iis.gender:
		score += 100
	if ps.faculty == iis.faculty:
		score += 100

	if ps.lang1:
		if ps.lang1 == iis.lang1 or ps.lang1 == iis.lang2 or ps.lang1 == iis.lang3:
			score += 20
	if ps.lang2:
		if ps.lang2 == iis.lang1 or ps.lang2 == iis.lang2 or ps.lang2 == iis.lang3:
			score += 20
	if ps.lang3:
		if ps.lang3 == iis.lang1 or ps.lang3 == iis.lang2 or ps.lang3 == iis.lang3:
			score += 20

	score -= math.fabs(ps.dob.year - iis.dob.year)
	return score