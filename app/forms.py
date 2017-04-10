from flask_wtf import Form
from wtforms import RadioField

class SongForm(Form):
	song_id = RadioField('Song Choice', coerce=int)
