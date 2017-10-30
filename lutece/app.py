# encoding: utf-8
u"""Lutéce application"""

from __future__ import print_function
from __future__ import unicode_literals
from os import path

from flask import Flask, render_template

from lutece.configurator import AssetConfigurator


# pylint: disable=invalid-name
manifest_json = path.join(path.dirname(__file__), '../static/manifest.json')

app = Flask(__name__, static_folder='../static', static_url_path='')

config = AssetConfigurator(manifest_json)
config.init_app(app)
# pylint: enable=invalid-name


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
