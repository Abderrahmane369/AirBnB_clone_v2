#!/usr/bin/python3
"""looogarihm"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """aaaaa"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """states"""
    states = storage.all(State)
    strg = storage.__class__.__name__
    return render_template('8-cities_by_states.html', slist=states, strg=strg)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
