#!/usr/bin/python3
"""looogarihm"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """aaaaa"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """states"""
    amenities = storage.all(Amenity)
    states = storage.all(State)

    return render_template('100-hbnb.html',
                           states=states, amenities=amenities, places=places)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
