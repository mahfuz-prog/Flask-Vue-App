from flask_cors import CORS
from flask import request, Blueprint, jsonify, abort, current_app
from flaskapp.users.utils import datastring_required
from flaskapp.db_models import User, Refer
from flaskapp import db

users = Blueprint('users', __name__, url_prefix='/api')
CORS(users)

@users.route('/')
@datastring_required
def home(current_user):
	if request.method == 'GET':
		data = 'This is Homepage'

	import time
	time.sleep(1)
	return jsonify(data)