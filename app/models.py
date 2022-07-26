from flask_sqlalchemy import SQLAlchemy
from app import db

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Model | id : {self.id} | name : {self.name}>"