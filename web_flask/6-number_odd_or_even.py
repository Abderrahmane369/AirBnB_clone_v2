#!/usr/bin/python3
"""azeaeaeaeaeae"""
from flask import Flask, render_template
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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """aheloow"""
    return str(n) + " is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """aheloow"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """aheloow"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run()
