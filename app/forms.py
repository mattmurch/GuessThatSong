from flask_wtf import Form
from wtforms import RadioField, StringField, PasswordField, validators


class SongForm(Form):
    """This class defines the multiple-choice form for selecting a song."""
    song_id = RadioField('Song Choice', coerce=int)


#~ class LoginForm(Form):
    #~ """This class defines the user login form."""
    #~ username = StringField('username', [validators.DataRequired()])
    #~ password = PasswordField('password', [validators.DataRequired()])
