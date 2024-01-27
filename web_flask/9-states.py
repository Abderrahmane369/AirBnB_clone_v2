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


@app.route('/states', strict_slashes=False)
def states():
    """states"""
    sttes = storage.all(State)
    return render_template('7-states_list.html', slist=sttes)


@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """states"""
    state = None
    if id:
        state = storage.all(State).get(f'State.{id}')
    return render_template('9-states.html', state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
