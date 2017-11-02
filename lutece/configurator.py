# encoding: utf-8
import json
from os import path
import sys

from bleach import clean
from markupsafe import Markup


class AssetConfigurator(object):
    """Configure class for asset files are built via webpack.

    This provides `built_asset_file` method to get filename from
    manifest.json.
    """

    def __init__(self, _manifest_json):  # (str) -> None
        self._app = None
        self._manifest_json = _manifest_json

        self._assets = {}

    @property
    def assets(self):
        return self._assets

    def init_app(self, _app):  # -> None
        """Loads manifest.json and appends a template global function."""
        self._app = _app
        self._load_manifest_json()

        _app.add_template_global(self.built_asset_file)
        _app.add_template_global(self.svg_content)

    def _load_manifest_json(self):  # () -> None
        try:
            with self._app.open_resource(self._manifest_json, 'r') as fh:
                self._assets = json.load(fh)
        except IOError:
            pass

    def built_asset_file(self, filepath):  # (str) -> str
        """Returns built asset file name if it is in manifest.json."""
        if sys.version_info[0] < 3:
            key = filepath.encode()
        else:
            key = filepath

        if key not in self.assets:
            return filepath

        return '{0}'.format(self.assets[key])

    def svg_content(self, filepath):  # (str) -> str
        """Returns svg content from filepath."""
        svg_file = path.join(
            path.dirname(__file__), '..', 'static',
            self.built_asset_file(filepath))

        content = ''
        try:
            with open(svg_file) as f:
                content = f.read()
        except IOError:
            pass

        return Markup(clean(content, tags=['symbol', 'defs', 'path'],
                            attributes=['id', 'd']))
