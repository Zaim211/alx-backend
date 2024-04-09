#!/usr/bin/env python3
""" Basic Flask app """

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """ setup flask app,
    hnadle / route
    """
    return render_template('0.index.html')


if __name__ == '__name__':
    app.run(port="3000", host='0.0.0.0', debug=True)
