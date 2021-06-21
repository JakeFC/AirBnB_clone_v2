#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns display text for '/' route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns display text for '/hbnb' route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_(text):
    """returns variable display text for '/c/<text>' variable route"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_(text):
    """returns variable display text for '/python/<text>' variable route,
    with 'is cool' set as default string
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_(n):
    """returns display text for '/number/<n>' variable route only if n
    is a number
    """
    return ('{} is a number'.format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_(n):
    """returns html page  for '/number_template/<n>' variable route only if n
    is a number
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even_(n):
    """returns html page  for '/number_odd_or_even/<n>' variable route only if n
    is a number
    """
    if n % 2:
        parity = 'odd'
    else:
        parity = 'even'
    return render_template('6-number_odd_or_even.html', n=n, parity=parity)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
