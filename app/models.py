#~ from flask_login import UserMixin

from app import db


class Songs(db.Model):
    """This class defines the Songs table in the database which holds the path of each
    song in the music directory. One column for the path with spaces, and one column where
    the spaces have been replaced by underscores.
    """
    id = db.Column(db.Integer, primary_key=True)
    path_sans_space = db.Column(db.String(120), index=True, unique=True)
    path_with_space = db.Column(db.String(120), index=True, unique=True)
    
    def __repr__(self):
        return '<Song %r>' % (self.path_with_space)


#~ class User(UserMixin):
    #~ """This class defines the User table in the database which holds the user login
    #~ credentials (Username and Password).
    #~ """
    #~ def __init__(self, username, password):
        #~ self.username = username
        #~ self.password = password
#~ 
    #~ def __repr__(self):
        #~ return "%s/%s" % (self.username, self.password)
