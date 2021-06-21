#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
import operator
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception=None):
    """removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """returns a dynamic web page for '/states_list' route"""
    return render_template('7-states_list.html', states=sorted(storage.all
                           (State).values(), key=operator.attrgetter('name')))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
