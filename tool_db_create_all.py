"""


@author  : zhouhuajian
@version : v1.0
"""
from flask import Flask, redirect
from db.test import db
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db.app = app
db.init_app(app)

if __name__ == '__main__':
    db.create_all()

