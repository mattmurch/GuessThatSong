import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import MUSICDIR

#Initialize flask app and database
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models

db.create_all()


def get_song_dir(musicdir=MUSICDIR):
    """Walks configured music directory for mp3 and flac files. Creates a row in the Songs
    table for each song found that is not already in the database.
    """
    abs_song_dirs = []
    rel_song_dirs = []
    unicode_musicdir = unicode(musicdir)
    for path, subdirs, files in os.walk(unicode_musicdir):
        for name in files:
            if name.endswith('.mp3') or name.endswith('.flac'):
                abs_song_dirs.append(os.path.join(path, name))
    for abs_directory in abs_song_dirs:
        rel_song_dirs.append(unicode(os.path.relpath(abs_directory, unicode_musicdir)))
    for rel_directory in rel_song_dirs:
        current_song = models.Songs.query.filter_by(path_with_space=rel_directory).first()
        if current_song is None:
            song = models.Songs(path_sans_space=rel_directory.replace(' ','_'), path_with_space=rel_directory)
            db.session.add(song)
            db.session.commit()

#On running the server, asks if it should run get_song_dir to update the database
update_db = raw_input("Would you like to update database?")
if update_db.startswith('y' or 'Y'):
    get_song_dir()
