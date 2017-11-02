# encoding: utf-8
u"""Lutéce application."""

from __future__ import print_function
from __future__ import unicode_literals
from os import path

from flask import Flask, render_template

from lutece.configurator import AssetConfigurator


# pylint: disable=invalid-name
manifest_json = path.join(path.dirname(__file__), '../static/manifest.json')

app = Flask(__name__, static_folder='../static', static_url_path='')

# development
# app.config['DEBUG'] = True
# app.config['TEMPLATES_AUTO_RELOAD'] = True

config = AssetConfigurator(manifest_json)
config.init_app(app)
# pylint: enable=invalid-name


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/philosophy')
def philosophy():
    return render_template('philosophy.html')


@app.route('/history')
def history():
    return render_template('history.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.errorhandler(404)
def not_found(_error):
    return render_template('errors/not_found.html'), 404


@app.errorhandler(500)
def server_error(_error):
    return render_template('errors/internal_server_error.html'), 500
