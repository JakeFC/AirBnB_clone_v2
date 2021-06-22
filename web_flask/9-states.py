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


@app.route('/states', strict_slashes=False)
def states():
    """returns a dynamic web page for '/states' route"""
    return render_template('9-states.html', states=storage.all(State))


@app.route('/states/<id>', strict_slashes=False)
def states_(id):
    """returns a dynamic web page for '/states/<id>' route"""
    state = None
    for obj in storage.all(State).values():
        if obj.id == id:
            state = obj
    return render_template('9-states.html', states=None, state=state)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
