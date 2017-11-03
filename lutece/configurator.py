# encoding: utf-8
import json
from os import path
import re
import sys

from bleach import clean
from markupsafe import Markup


def rescue_svg_path(content):
    """Rescues broken tags by `bleach.clean` (built in html5lib)."""
    svg_content = re.sub(r'\</path\>', '', content)
    return re.sub(r'(\<path[A-z\s=\"-\.0-9]*")(\s*\>)', "\\1/\\2",
                  svg_content)


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
        _app.add_template_global(self.svg_icons)

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

    def _load_svg(self, filepath, sub_directory='', **kwargs):
        # (str, str, dict) -> str
        """Returns svg content from filepath (if it exists).

        manifest.json has only filename as key. If NODE_ENV is not `production`
        (manifest.json does not exist), svg will be found in sub_directory.

        The content of manifest.json looks like:
        ```
        {
          "master.svg": "img/master.0123456789.svg"
        }
        ```
        """
        asset_file = self.built_asset_file(filepath)
        if path.basename(asset_file) == filepath:
            # built in NODE_ENV=development
            asset_file = path.join(sub_directory, filepath)

        svg_file = path.join(
            path.dirname(__file__), '..', 'static', asset_file)

        content = ''
        try:
            with open(svg_file, 'r') as f:
                content = f.read()
        except IOError:
            return ''

        return Markup(clean(content, **kwargs))

    def svg_icons(self, filepath):
        """Returns svg icon tags.

        >>> from lutece.configurator import AssetConfigurator
        >>> c = AssetConfigurator('path/to/manifest.json')

        `icon.svg` file must be in `static/img` directory.
        The usage in template looks like that.

        ```
        {{svg_icons('file.svg')|safe}}
        ```

        >>> c.svg_icons('icon.svg')
        ''
        """
        return rescue_svg_path(self._load_svg(
            filepath,
            sub_directory='img',
            tags=['symbol', 'defs', 'path'],
            attributes={
                'symbol': ['id'],
                'path': ['id', 'd', 'transform']
            }))
