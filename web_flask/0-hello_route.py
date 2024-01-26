#!/usr/bin/python3
"""azeaeaeaeaeae"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """aheloow"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run()
