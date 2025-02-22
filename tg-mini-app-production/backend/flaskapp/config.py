import json

with open('/etc/config.json') as config_file:
	config = json.load(config_file)

class Config():
	SECRET_KEY = config.get('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')

	BOT_TOKEN = config.get('BOT_TOKEN')
	BOT_TOKEN_TIMEOUT = 30 	# In minutes
	AUTHORIZATION_PREFIX = config.get('AUTHORIZATION_PREFIX')