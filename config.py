import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))
MUSICDIR = os.path.join(BASEDIR, 'app/static')
CSRF_ENABLED = True
SECRET_KEY = 'nevergraduate'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
