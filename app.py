from flask import Flask, redirect
from page.test import bp as test_bp
from api.test import bp as api_test_bp
from db.test import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.register_blueprint(test_bp)
app.register_blueprint(api_test_bp)
db.init_app(app)

@app.route('/', methods=['GET'])
def index():
    return redirect('/test/data')



if __name__ == '__main__':
    app.run(port=80, debug=True)