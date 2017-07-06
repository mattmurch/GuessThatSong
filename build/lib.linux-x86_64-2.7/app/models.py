from flask_login import UserMixin

from app import db


class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path_sans_space = db.Column(db.String(120), index=True, unique=True)
    path_with_space = db.Column(db.String(120), index=True, unique=True)
    
    def __repr__(self):
        return '<Song %r>' % (self.path_with_space)


class User(UserMixin):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "%s/%s" % (self.username, self.password)
