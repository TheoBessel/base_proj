from app import app, db
from app.models import *

if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    db.session.add(Model("Base Model"))
    db.session.commit()
    app.run(debug=True)