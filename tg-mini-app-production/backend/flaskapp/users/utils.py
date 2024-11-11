import json
import hmac
import hashlib
import datetime
from flaskapp import db
from functools import wraps
from urllib.parse import unquote
from flaskapp.db_models import User, Refer
from flask import request, abort, current_app

def datastring_required(f):
	"""Decorator to enforce data string validation and user authentication.

	This decorator ensures that the incoming request has a valid 'Authorization' header
	with a AUTHORIZATION_PREFIX and a data string. It validates the data string and authenticates
	the user before calling the decorated route.

	Args:
		f: The function to be decorated.

	Returns:
		The decorated function.
	"""
	
	@wraps(f)
	def wrapper(*args, **kwargs):
		data_string = None
		if (('Authorization' in request.headers) and 
			(current_app.config['AUTHORIZATION_PREFIX'] in request.headers['Authorization']) and
			(len(request.headers['Authorization']) > len(current_app.config['AUTHORIZATION_PREFIX']))):

			pre, string = request.headers['Authorization'].split(' ')
			if pre == current_app.config['AUTHORIZATION_PREFIX']:
				data_string = string
				
		if not data_string:
			abort(403)

		status, data_string_dict = validate_init_data(data_string, current_app.config['BOT_TOKEN'])
		if status:
			current_user = handle_reg_login(data_string_dict)
		else:
			abort(401)

		return f(current_user, *args, **kwargs)
	return wrapper


'''https://docs.telegram-mini-apps.com/platform/init-data#validating'''
def validate_init_data(init_data: str, bot_token: str):
	vals = {k: unquote(v) for k, v in [s.split('=', 1) for s in init_data.split('&')]}
	data_check_string = '\n'.join(f"{k}={v}" for k, v in sorted(vals.items()) if k != 'hash')

	# set the functionality for expire the token
	create_time = datetime.datetime.fromtimestamp(int(vals['auth_date']))
	timeout = create_time + datetime.timedelta(minutes=current_app.config['BOT_TOKEN_TIMEOUT'])
	if datetime.datetime.utcnow() >= timeout:
		return False, None

	secret_key = hmac.new("WebAppData".encode(), bot_token.encode(), hashlib.sha256).digest()
	h = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256)
	return h.hexdigest() == vals['hash'], vals


# create user if not registered
# return user if user found in database
def handle_reg_login(data_string_dict):
	user_info = json.loads(data_string_dict['user'])
	tg_id = user_info['id']
	name = user_info['first_name'] + ' ' + user_info['last_name']

	if 'query_id' in data_string_dict.keys():
		''''https://core.telegram.org/bots/api#answerwebappquery,
		if only the telegram web application open through attachment 
		menu button then query_id added to data_straing'''

		query_id = data_string_dict['query_id']


	# if the user already exist return the user
	# it will work as login functionality
	user = User.check_tg_id(tg_id)
	if user:
		return user


	# registration functionality
	if 'start_param' in data_string_dict.keys():
		'''referral functionality
		https://t.me/ownairdrop_bot/oab,
		https://t.me/ownairdrop_bot/oab?startapp=ref_6667576529
		startapp contain the value of start_param
		'''

		start_param = data_string_dict['start_param'][4:]
		user = User.check_tg_id(start_param)
		if user:
			'''if parent user found from the refer id in the database
			then create a refer in the database for parent user.
			create and return new user
			'''

			refer_user = Refer(tg_id=tg_id, line=user)
			db.session.add(refer_user)
			db.session.commit()
			return create_user(tg_id, name)

		'''if there no user found from the refer id then create and return the user'''
		return create_user(tg_id, name)

	'''if there is not start_param create and return user'''
	return create_user(tg_id, name)


def create_user(tg_id, name):
	'''create user in database and return

	Args:
		tg_id: Telegram id.
		name: Telegram username

	Returns:
		created user
	'''

	add_user = User(tg_id=tg_id, username=name)
	db.session.add(add_user)
	db.session.commit()
	return add_user