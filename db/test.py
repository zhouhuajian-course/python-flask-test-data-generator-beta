"""


@author  : zhouhuajian
@version : v1.0
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(engine_options={"echo": True})
class TestData(db.Model):
    __tablename__ = 'test_data'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    type = db.Column(db.String, nullable=False)  # 数据类型 text或file
    size = db.Column(db.Integer, nullable=False)  # 数据大小
    data = db.Column(db.String, nullable=False)  # 具体数据
    def __repr__(self):
        return f"TestData(id={self.id}, type={self.type}, size={self.size}, data={self.data})"

