"""


@author  : zhouhuajian
@version : v1.0
"""
import mimetypes
import os

from flask import Blueprint, render_template, make_response

bp = Blueprint('test', __name__)
from db.test import TestData

@bp.route('/test/data', methods=['GET'])
def data():
    rows = TestData.query.order_by(TestData.id.desc()).limit(100).all()
    # print(test_data)
    return render_template('test/data.html', rows=rows)

@bp.route('/test/file/<int:test_data_id>', methods=['GET'])
def file(test_data_id):
    test_data: TestData = TestData.query.get(test_data_id)
    content = os.urandom(test_data.size)
    filename = test_data.data
    response = make_response(content)
    mime_type = mimetypes.guess_type(filename)[0]
    response.headers['Content-Type'] = mime_type
    response.headers['Content-Disposition'] = 'attachment; filename={}'.format(filename.encode().decode('latin-1'))
    return response
