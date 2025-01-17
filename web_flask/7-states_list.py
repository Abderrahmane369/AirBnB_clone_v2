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


@app.route('/states_list', strict_slashes=False)
def states_list():
    """states"""
    states = storage.all(State)
    return render_template('7-states_list.html', slist=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
