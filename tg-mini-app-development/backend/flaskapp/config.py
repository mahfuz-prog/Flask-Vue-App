import os

class Config():
	SECRET_KEY = 'hola'
	SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"

	BOT_TOKEN = os.environ.get('BOT_TOKEN')
	BOT_TOKEN_TIMEOUT = 1 	# In minutes
	AUTHORIZATION_PREFIX = 'tma'

	# MAIL_SERVER configuration
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 465
	MAIL_USERNAME = os.environ.get('EMAIL_USER') 	#email
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')	#app password
	MAIL_USE_TLS = False
	MAIL_USE_SSL = True