#!/usr/bin/python3
"""azeaeaeaeaeae"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """aheloow"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """aheloow"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def txt(text):
    """aheloow"""
    return "C " + escape(text).replace('_', ' ')


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python(text='is cool'):
    """aheloow"""
    return "Python " + escape(text).replace('_', ' ')


if __name__ == '__main__':
    app.run()
