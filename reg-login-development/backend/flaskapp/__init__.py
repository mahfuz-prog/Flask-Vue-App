from flask import Flask
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flaskapp.config import Config

db = SQLAlchemy()
mail = Mail()
bcrypt = Bcrypt()

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(config_class)

	db.init_app(app)
	mail.init_app(app)
	bcrypt.init_app(app)

	from flaskapp.users.routes import users
	app.register_blueprint(users)
	
	return app