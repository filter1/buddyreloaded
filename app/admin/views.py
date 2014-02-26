from flask import Blueprint, flash, redirect, render_template, request, url_for

# from app.data import db


admin = Blueprint('admin', __name__)


@users.route('/login/', methods=('GET', 'POST'))
def admin_index():
	return render_template('users/login.html', form=form)

