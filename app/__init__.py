# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from flask_login import LoginManager

app = Flask(__name__)

#Configuration of application, see configuration.py, choose one and uncomment.
#app.config.from_object('configuration.ProductionConfig')
app.config.from_object('app.configuration.DevelopmentConfig')
app.config.from_pyfile('instance/config.py')
#app.config.from_object('configuration.TestingConfig')

bs = Bootstrap(app) #flask-bootstrap
db = SQLAlchemy(app) #flask-sqlalchemy
lm = LoginManager()
lm.setup_app(app)
lm.login_view = 'login'

print("init")

from app import views, models
from app.models import TestModel

def init_db():
    db.create_all()

    # Create a test user
    new_user = TestModel(name='Morteza')
    db.session.add(new_user)
    db.session.commit()
    print("first user created")
init_db()

