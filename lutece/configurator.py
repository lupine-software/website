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
        """Returns built asset file name if it is in manifest.json.

        >>> from lutece.configurator import AssetConfigurator
        >>> c = AssetConfigurator('path/to/manifest.json')
        >>> c._assets = {'bundle.svg': 'bundle.0123456789.svg'}

        >>> c.built_asset_file('bundle.svg')
        'bundle.0123456789.svg'
        """
        if sys.version_info[0] < 3:
            key = filepath.encode()
        else:
            key = filepath

        if key not in self.assets:
            return filepath

        return '{0}'.format(self.assets[key])

    def svg_content(self, filepath, sub_directory=''):  # (str) -> str
        """Returns svg content from filepath.

        manifest.json has only filename as key. If NODE_ENV is not `production`
        (manifest.json does not exist), svg will be found in sub_directory.

        manifest.json:
            production: {"master.svg": "img/master.xxx.svg"}
            development: none

        >>> from lutece.configurator import AssetConfigurator
        >>> c = AssetConfigurator('path/to/manifest.json')

        >>> c.svg_content('bundle.svg', 'img')
        ''
        """

        asset_file = self.built_asset_file(filepath)
        if path.basename(asset_file) == filepath:
            # built in NODE_ENV=development
            asset_file = path.join(sub_directory, filepath)

        svg_file = path.join(
            path.dirname(__file__), '..', 'static', asset_file)

        content = ''
        try:
            with open(svg_file) as f:
                content = f.read()
        except IOError:
            return ''

        return Markup(clean(content, tags=['symbol', 'defs', 'path'],
                            attributes=['id', 'd']))
