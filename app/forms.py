from flask_wtf import Form
from wtforms import RadioField, StringField, PasswordField, validators


class SongForm(Form):
    song_id = RadioField('Song Choice', coerce=int)


class LoginForm(Form):
    username = StringField('username', [validators.DataRequired()])
    password = PasswordField('password', [validators.DataRequired()])
