"""Flask demo."""
import os
from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

basedir = os.path.abspath(os.path.dirname(__file__))

# + os.path.join(basedir, 'test.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:xiezhibin@' +\
    'localhost/test?charset=utf8'
db = SQLAlchemy()
db.init_app(app)
manager = Manager(app)


class Table(db.Model):
    """Table model."""

    __tablename__ = 'table'
    username = db.Column(db.String(128), primary_key=True)
    password = db.Column(db.String(128))


@app.route('/')
def index():
    """Index."""
    row = Table.query.first()
    resp = {
        'data': [1, 2, 4, 5],
        'status': 0,
        'username': row.username
    }
    return jsonify(resp)


@app.route('/test')
def test():
    """."""
    resp = """{
        "data":[1, 2, 3],
        "status": 12
    }"""
    resp = make_response(resp)
    resp.headers['Content-Type'] = 'application/json'
    return resp


@app.route('/sql')
def raw_sql():
    """."""
    sql = "select * from `table` where username = :UN"
    params = {
        'UN': 'asdfa'
    }
    data = db.session.execute(sql, params)
    data = data.fetchone()
    print(data)
    return data[0]

if __name__ == '__main__':

    manager.run()
