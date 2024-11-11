import jwt
import datetime
from flask_cors import CORS
from flaskapp import db, bcrypt
from flaskapp.db_models import User
from flaskapp.users.messages import send_otp
from flask import request, Blueprint, jsonify, abort, current_app
from flaskapp.users.utils import (login_required, generate_otp, create_hmac, verify_hmac, logout_required)

# create bluprint instance
users = Blueprint('users', __name__, url_prefix='/api')
CORS(users)

@users.route('/')
def home():
	if request.method == 'GET':
		data = 'This is Homepage'

	import time
	time.sleep(3)
	return jsonify(data)


@users.route('/sign-up/', methods=['POST'])
@logout_required
def sign_up():
	if request.method == 'POST':
		response = request.get_json()
		name = response['name']
		email = response['email']

		# check if the username and email in the database
		name_status = User.check_name(name)
		email_status = User.check_email(email)

		# data store error values
		# if error occur data will send to frontend
		data = {}
		if name_status:
			data.update({ 'nameStatus' : 'Username already taken! Please try another one.' })
		
		if email_status:
			data.update({ 'emailStatus' : 'Email already taken!'})

		# if there is no error then create a otp and get the hmac.
		# rewrite the data variable with hmac and send to frontend
		if not data:
			otp = generate_otp()
			is_sent = send_otp(otp, email)

			if is_sent:
				data = create_hmac(response, current_app.config['SECRET_KEY'], otp)
			else:
				data.update({'emailSentStatus':is_sent})

	return jsonify(data)


@users.route('/verify/', methods=['POST'])
@logout_required
def verify():
	if request.method == 'POST':
		response = request.get_json()
		info = response['info']
		otp = response['otp']
		hmac_ = response['hmac']

		name = response['info']['name']
		email = response['info']['email']
		password = response['info']['password']

		is_verified = verify_hmac(info, current_app.config['SECRET_KEY'], otp, hmac_)

		if not is_verified:
			abort(401)

		# in verification process if other user take the username
		# in this case db throw unique constraint error
		if not (User.check_name(name) and User.check_email(email)):
			hashed_pass = bcrypt.generate_password_hash(password, rounds=13).decode('utf-8')
			user = User(username=name, email=email, password=hashed_pass)
			db.session.add(user)
			db.session.commit()
		else:
			abort(401)

	return jsonify('verified')


# login functionality
@users.route('/log-in/', methods=['POST'])
@logout_required
def login():
	if request.method == 'POST':
		response = request.get_json()
		email = response['email']
		password = response['password']

		data = {}
		user = User.query.filter_by(email=email).first()
		if user and bcrypt.check_password_hash(user.password, password):
			token = jwt.encode(
						{
							'id' : user.id, 
							'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=current_app.config['JWT_TIMEOUT'])
						}, current_app.config['SECRET_KEY'], algorithm="HS256")

			data.update({ 'token' : token })
		else:
			data.update({ 'error' : 'Bad Credentials' })

	return data


# verify a exixting jwt token
@users.route('/login-check/')
@login_required
def login_check(current_user):
	return jsonify(current_user.id)

# account page
@users.route('/account/')
@login_required
def account(current_user):
	user = {
		'name' : current_user.username,
		'email' : current_user.email
	}
	return jsonify(user)