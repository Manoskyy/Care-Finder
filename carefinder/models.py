from . import db
from flask_login import UserMixin, current_user
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
import uuid


#=============User table==================
class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(120), nullable=False)
	last_name = db.Column(db.String(120), nullable=False)
	email = db.Column(db.String(50), unique=True, nullable=False)
	password = db.Column(db.String(120), nullable=False)
	timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
	role = db.Column(db.String(50), nullable=False, default='normal')
	phone = db.Column(db.String(120), nullable=True)
	city = db.Column(db.String(120), nullable=True)

	def __repr__(self):
		return '<User %r>' % self.first_name

	#===========User method for converting the user password in to a hash password===========
	def set_password(self, password):
		hash_password = generate_password_hash(password)
		self.password = hash_password

	#===========Verifying password typed by user when logging in by comparing it to the already stored password===========
	def verify_password(self, password):
		return check_password_hash(self.password, password)