"""
创建数据库表

@author  : zhouhuajian
@version : v1.0
"""
from flask import Flask
from db.test import db

# Flask 应用
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db.app = app
db.init_app(app)

if __name__ == '__main__':
    # create_all 创建所有表 SQLite会自动创建数据库
    # https://docs.sqlalchemy.org/en/14/core/metadata.html?highlight=create_all#sqlalchemy.schema.MetaData.create_all
    db.create_all()
