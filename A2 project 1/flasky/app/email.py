from flask.ext.mail import Message
from flask import render_template
from app import mail


# SUBJECT_PREFIX = '[FLASKY]'
# SENDER = 'Flasky Admin <flasky@example.com>'

SUBJECT_PREFIX = '[FLASKY]'
SENDER = 'Flasky Admin <flasky@example.com>'

def send_email(to, subject, template, **kwargs):
	msg = Message(SUBJECT_PREFIX + subject,\
					sender = SENDER, recipients = [to])
	msg.body = render_template(template + '.txt', **kwargs)
	#msg.html = render_template(template + '.html', **kwargs)
	mail.send(msg)
