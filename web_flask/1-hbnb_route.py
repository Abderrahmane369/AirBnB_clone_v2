#!/usr/bin/python3
"""azeaeaeaeaeae"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """aheloow"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """aheloow"""
    return "HBNB"


if __name__ == '__main__':
    app.run()
