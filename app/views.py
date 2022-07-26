from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from app import app, db
from app.models import *

@app.route('/')
@app.route('/index')
def index():
    return render_template('./index.html')

if __name__ == "__main__":
    app.run(debug=True)