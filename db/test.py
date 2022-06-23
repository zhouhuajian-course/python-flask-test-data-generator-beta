"""
测试数据库

@author  : zhouhuajian
@version : v1.0
"""
from flask_sqlalchemy import SQLAlchemy

# 数据库db对象
db = SQLAlchemy(engine_options={"echo": True})


class TestData(db.Model):
    """测试数据 Model"""

    __tablename__ = 'test_data'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    type = db.Column(db.String, nullable=False)  # 数据类型 text或file
    size = db.Column(db.Integer, nullable=False)  # 数据大小
    data = db.Column(db.String, nullable=False)  # 具体数据

    def __repr__(self):
        """对象描述"""
        return f"TestData(id={self.id}, type={self.type}, size={self.size}, data={self.data})"
