import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))
MUSICDIR = '/media/matt/1FE5C2761C3B90D6/Users/Matt Murch/Music'
CSRF_ENABLED = True
SECRET_KEY = 'nevergraduate'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'db_repository')
