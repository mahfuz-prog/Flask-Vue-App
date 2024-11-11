import json

with open('/etc/config.json') as config_file:
	config = json.load(config_file)

class Config():
	SECRET_KEY = config.get('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
	JWT_TIMEOUT = 1		# In minutes
	OTP_TIMEOUT = 2		# In minutes

	# MAIL_SERVER configuration
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 465
	MAIL_USERNAME = config.get('EMAIL_USER') 	#email
	MAIL_PASSWORD = config.get('EMAIL_PASS')	#app password
	MAIL_USE_TLS = False
	MAIL_USE_SSL = True