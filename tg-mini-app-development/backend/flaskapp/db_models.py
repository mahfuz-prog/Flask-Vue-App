from flaskapp import db
from datetime import datetime

class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	tg_id = db.Column(db.Integer, unique=True, nullable=False)
	username = db.Column(db.String(30), unique=True, nullable=False)
	email = db.Column(db.String(30), unique=True, nullable=True)
	date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	refers = db.relationship('Refer', backref='line', lazy=True)

	# username check while creating account
	@staticmethod
	def check_tg_id(tg_id):
		try:
			user = User.query.filter_by(tg_id=tg_id).first()
			if user:
				return user
			return False
		except:
			return False

	def __repr__(self):
		return f'< username: {self.username} | telegram_id: {self.tg_id} >'


class Refer(db.Model):
	__tablename__ = 'refer'
	id = db.Column(db.Integer, primary_key=True)
	tg_id = db.Column(db.Integer, unique=True, nullable=False)
	referrer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f'< telegram_id: {self.tg_id} >'