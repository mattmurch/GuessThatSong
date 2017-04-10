import os
basedir = os.path.abspath(os.path.dirname(__file__))
musicdir = '/media/matt/1FE5C2761C3B90D6/Users/Matt Murch/Music'

CSRF_ENABLED = True
SECRET_KEY = 'pooper-scooper'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
