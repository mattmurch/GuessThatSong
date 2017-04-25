from app import db
from flask_login import UserMixin

class Songs(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	path_sans_space = db.Column(db.String(120), index=True, unique=True)
	path_with_space = db.Column(db.String(120), index=True, unique=True)
	
	def __repr__(self):
		return '<Song %r>' % (self.path_with_space)
		
class User(UserMixin):
	#~ id = db.Column(db.Integer, primary_key=True)
	#~ username = db.Column(db.String(120), index=True, unique=True)
	#~ password = db.Column(db.String(120), index=True, unique=True)
	def __init__(self, id):
		self.id = id
		self.username = "user" + str(id)
		self.password = self.username + "_secret"
		
	def __repr__(self):
		return "%d/%s/%s" % (self.id, self.username, self.password)
