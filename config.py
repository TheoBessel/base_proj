import os

SECRET_KEY = "SECRET_KEY"
APP_ID = 00000
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://') or 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')