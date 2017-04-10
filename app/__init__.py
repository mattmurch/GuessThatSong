import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import basedir
from config import musicdir

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models

#returns a list of the path of all music files in the given directory
def getSongDir(musicdir):
	abssongdirs = []
	relsongdirs = []
	unicodemusicdir = unicode(musicdir)
	for path, subdirs, files in os.walk(unicodemusicdir):
		for name in files:
			if name.endswith('.mp3') or name.endswith('.flac'):
				abssongdirs.append(os.path.join(path, name))
	for x in abssongdirs:
		relsongdirs.append(unicode(os.path.relpath(x, unicodemusicdir)))
	for x in relsongdirs:
		currentsong = models.Songs.query.filter_by(path_with_space=x).first()
		if currentsong is None:
			song = models.Songs(path_sans_space=x.replace(' ','_'), path_with_space=x)
			db.session.add(song)
			db.session.commit()

update_db = raw_input("Would you like to update database?")
if update_db.startswith('y' or 'Y'):
	getSongDir(musicdir)

#~ from .models import Songs
#~ 
#~ #iterates through all the songs in songlist and adds them as entries to Songs table
#~ for x in songlist:
	#~ if not Songs.query.filter_by(path_with_space = x):
		#~ song = Songs(path_sans_space=x.replace(' ','_'), path_with_space=x)
		#~ db.session.add(song)
		#~ db.session.commit()
