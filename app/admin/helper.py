import traceback
from flask.ext.mail import Message, Mail

from app.mails import mail
from app.data import db
from app.decorators import async

@async
def send_email_to_matching(matchings): 
	with mail.connect() as conn:
				try:
					for pair in matchings:
						message = render_template("admin/email_to_iis.txt", iis = pair.iis, ps = pair.ps)
						subject = "[Buddy] You have a Buddy!"
						msg = Message(
							recipients=[pair.iis.email],
							cc=["contact@buddy-md.de"],
							sender="contact@buddy-md.de",
						  body=message,
						  subject=subject)
						conn.send(msg)

						message = render_template("admin/email_to_ps.txt", iis = pair.iis, ps = pair.ps)
						subject = "[Buddy] You have a Buddy!"
						msg = Message(
							recipients=[pair.ps.email],
							cc=["contact@buddy-md.de"],
							sender="contact@buddy-md.de",
						  body=message,
						  subject=subject)
						conn.send(msg)

						pair.email_send = True
				except Exception, e:
					print "Fail: %s" % e
					traceback.print_exc()
			db.session.commit()