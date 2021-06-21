#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
import operator
from models import storage
from models.state import State
from os import getenv

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception=None):
    """removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """returns a dynamic web page for '/cities_by_states' route"""
    states = sorted(storage.all(State).values(), key=operator.attrgetter
                    ('name'))
    return render_template('8-cities_by_states.html', states=states,
                           storageT=getenv('HBNB_TYPE_STORAGE'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
