"""Flask demo."""
from flask import Flask, \
jsonify, make_response

app = Flask(__name__)


@app.route('/')
def index():
    """Index."""
    resp = {
        'data': [1, 2, 4, 5],
        'status': 0
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

if __name__ == '__main__':
    app.run(debug=True)
