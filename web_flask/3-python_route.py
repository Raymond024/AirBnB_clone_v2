#!/usr/bin/python3
"""
starts a Flask web application
that listens to 0.0.0.0, port 5000
"""

from flask import Flask
app = Flask(__name__)


@app.route('/hbnb_index', strict_slashes=False)
def hbnb_index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'

@app.route('/fun_c/<text>', strict_slashes=False)
def fun_c(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')

@app.route('/python_cool', strict_slashes=False)
@app.route('/python_cool/<text>', strict_slashes=False)
def python_cool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
