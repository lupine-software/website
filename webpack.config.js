'use strict';

var path = require('path')
  , webpack = require('webpack')
  , ExtractTextPlugin = require('extract-text-webpack-plugin')
  , ManifestPlugin = require('webpack-manifest-plugin')
  , LicenseWebpackPlugin = require('license-webpack-plugin')
  ;

var nodeEnv = process.env.NODE_ENV || 'production';
console.log('» webpack:', nodeEnv);

var appName = 'lutece';

var filename = '[name]';
if (nodeEnv == 'production') {
  filename += '.[contenthash]';
}
var stylusBundler = new ExtractTextPlugin(filename + '.css')
  , svgBundler = new ExtractTextPlugin('img/' + filename + '.svg')
  ;

var config = {
  output: {
    path: path.resolve(__dirname, 'tmp/build/')
  , filename: (nodeEnv == 'production' ? '[name].[chunkhash].js' : '[name].js')
  }
, module: {
    loaders: [{
      test: /\.css$/
    , loader: stylusBundler.extract(['css'])
    }, {
      test: /\.styl$/
    , loader: stylusBundler.extract(['css', 'stylus'])
    , include: [
        path.resolve(__dirname, appName, 'assets')
      ]
    }, {
      test: /\.svg$/
    , loader: svgBundler.extract(['svg-sprite'])
    , include: [
        path.resolve(__dirname,
          'node_modules/open-iconic/sprite/open-iconic.min.svg')
      ]
    , exclude: path.resolve(__dirname, appName, 'assets')
    }, {
      test: /\.(svg|png|woff|woff2|eot|ttf)$/
    , loader: 'url-loader?limit=100000'
    , exclude: /node_modules/
    }, {
      test: /\.js$/
    , loader: 'babel-loader'
    , include: [
        path.resolve(__dirname, appName, 'assets')
      ]
    }]
  }
, resolve: {
    extensions: ['', '.css', '.js', '.svg']
  , alias: {
      'open-iconic\.svg$': 'open-iconic/sprite/open-iconic.min.svg'
    , 'styr\.css$': 'styr/dst/styr.min.css'
    }
  }
, plugins: (function() {
    var _plugins = [
      stylusBundler
    , svgBundler
    ];
    _plugins.push(
      new webpack.EnvironmentPlugin([
       'NODE_ENV'
      ])
    );
    _plugins.push(
      new webpack.DefinePlugin({
        'process.env.NODE_ENV': JSON.stringify(nodeEnv)
      })
    );
    if (nodeEnv == 'production') {
      _plugins.push(
        new ManifestPlugin({
          fileName: 'manifest.json'
        })
      );
      _plugins.push(
        new LicenseWebpackPlugin({
          pattern: /^(MIT|ISC|BSD.*)$/
        , filename: 'freesoftware-licenses.txt'
        , addLicenseText: false
        , licenseFilenames: [
          // These filese are needed to check license in package.json.
            'LICENSE', 'LICENSE.md', 'LICENSE.txt'
          , 'license', 'license.md', 'license.txt'
          , 'README', 'README.md', 'README.txt'
          , 'readme', 'readme.md', 'readme.txt'
          ]
        })
      );
      _plugins.push(
        new webpack.optimize.UglifyJsPlugin({
          debug: false
        , minimize: true
        , compress: {
            warnings: false
          }
        , output: {
            comments: false
          }
        })
      );
    }
    return _plugins;
  })()
}

module.exports = config;
