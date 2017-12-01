# encoding: utf-8
u"""Lutéce application."""

from __future__ import print_function
from __future__ import unicode_literals
from os import path, getenv

from flask import Flask, render_template
from flask_sslify import SSLify

from lutece.config import CONFIG
from lutece.configurator import AssetConfigurator


def __configure(_app):
    # app.config
    CONFIG[getenv('ENV', 'production')].init_app(_app)

    # asset files
    manifest_json = path.join(
        path.dirname(__file__), '../static/manifest.json')
    asset = AssetConfigurator(manifest_json)
    asset.init_app(_app)

    # ssl support
    sslify = SSLify(_app, subdomains=True, skips=[
        # does not need first slash
        '_ah/health'
    ])
    sslify.init_app(_app)


# pylint: disable=invalid-name
app = Flask(__name__, static_folder='../static', static_url_path='')
__configure(app)
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
