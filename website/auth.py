from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .models import *

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form.get('email')
		passwd = request.form.get('pass')

		user = User.objects(email=email).first()
		if user:
			if check_password_hash(user.password, passwd):
				login_user(user, remember=True)
				flash('Logged in user', category='success')
				return redirect(url_for('views.home'))
			else:
				flash('You have entered an incorrect password', category='error')
		else:
			flash('Email addess is not recognized', category='error')
	# data = request.form
	return render_template("login.html", user=current_user)
 
@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('auth.login'))
 
@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		email = request.form.get('email')
		fName = request.form.get('firstName')
		lName = request.form.get('lastName')
		pass1 = request.form.get('pass1')
		pass2 = request.form.get('pass2')

		user = User.objects(email=email).first()
		if user:
			flash('This email is registered arleady',category='error')
		elif len(email) < 4:
			flash('Email is too short', category='error')
		elif len(fName) < 2:
			flash('Name must be longer than 1 character', category='error')
		elif pass1 != pass2:
			flash('Passwords don\'t match', category='error')
		elif len(pass1) < 5:
			flash('Password is too short', category='error')
		else:
			new_user = User(email=email, f_name=fName, l_name=lName, password=generate_password_hash(pass1, method='sha256'))
			new_user.save()
			login_user(user, remember=True)
			flash('User account created', category='success')
			return redirect(url_for('views.home'))
	return render_template("signup.html", user=current_user)
 