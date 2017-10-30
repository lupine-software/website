# encoding: utf-8
u"""Lut\xe8ce application"""
from __future__ import print_function
from __future__ import unicode_literals
import json
from os import path

from flask import Flask, render_template


class AssetConfigurator(object):
    """Configure class for asset files are built via webpack.

    This provides `built_asset_file` method to get filename from
    manifest.json.
    """
    def __init__(self, _manifest_json):  # (str) -> None
        self._app = None
        self._assets = {}
        self._manifest_json = _manifest_json

    def init_app(self, _app):  # -> None
        """Loads manifest.json and appends a template global function."""
        self._app = _app
        self._load_manifest_json()

        _app.add_template_global(self.built_asset_file)

    def _load_manifest_json(self):  # () -> None
        try:
            with self._app.open_resource(self._manifest_json, 'r') as fh:
                self._assets = json.load(fh)
        except IOError:
            pass

    def built_asset_file(self, filepath):  # (str) -> str
        """Returns built asset file name if it is in manifest.json."""
        key = filepath.encode()
        if key not in self._assets:
            return filepath
        return '{0}'.format(self._assets[key])


# pylint: disable=invalid-name
manifest_json = path.join(path.dirname(__file__), 'static/manifest.json')

app = Flask(__name__, static_folder='static', static_url_path='')

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


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
