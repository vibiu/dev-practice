"""Demo."""
from flask import Flask

app = Flask(__name__)

print("Name: " + __name__)


@app.route('/')
def test():
    """Test."""
    return "<h1>hello world</h1>"


app.run(debug=True, host="0.0.0.0")
