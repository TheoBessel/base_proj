import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sass

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
db.init_app(app)

sass.compile(dirname=('app/assets/scss', 'app/static/css'))

from app import views, models