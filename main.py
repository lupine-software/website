u"""Lut\xe8ce application"""
from __future__ import print_function
from __future__ import unicode_literals

from flask import Flask, render_template


# pylint: disable=invalid-name
app = Flask(__name__, static_folder='static', static_url_path='')


@app.route('/')
def home():
    """Home."""
    return render_template('index.html')


@app.errorhandler(404)
def not_found(_error):
    """Not Found."""
    return render_template('errors/not_found.html'), 404


@app.errorhandler(500)
def server_error(_error):
    """Internal Server Error."""
    return render_template('errors/internal_server_error.html'), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
