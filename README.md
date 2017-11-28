# Lutèce

`/lytɛs/`

[![pipeline status][pipeline]][commit] [![coverage report][coverage]][commit]

![Lupine Software LLC](lutece/assets/img/lupine-software-logo-300x300.png)

```txt
   _
\_|_)             \
  |          _|_  _   __   _
 _|    |   |  |  |/  /    |/
(/\___/ \_/|_/|_/|__/\___/|__/

Lutèce; LUpine sofTwarE website to introduCE about our products and ourselves
```

The website of [Lupine Software](https://lupine-software.com).


## Repository

[https://gitlab.com/lupine-software/lutece](
https://gitlab.com/lupine-software/lutece)


## Requirements

* Python `3.5` (or `2.7`)
* Node.js `>= 8.9.0` (build, npm `>= 5.5.1`)


## Setup

```zsh
: e.g. python3.5
: setup venv as you like (e.g. use nodeenv on Gentoo Linux)
% sudo emerge -av virtualenv (or just `sudo pip install virtualenv`)

% python3.5 -m venv venv
% source venv/bin/activate
(venv) % python -V
3.5

(venv) % pip install --upgrade pip setuptools
(venv) % pip install -r requirements.txt
```

#### Node.js

```
(venv) % pip install nodeenv
(venv) % nodeenv -p --node=8.9.0

(venv) % source venv27/bin/activate
(venv) % npm install -g npm@latest

(venv) % npm install -g gulp-cli
(venv) % npm install -g --engine-strict eslint @sonarwhal/sonar

: this runs also `gulp` after install
(venv) % npm install

: same as NODE_ENV=development gulp
(venv) % make build
```

### Dependencies

TODO


## Development

```zsh
(venv) % NODE_ENV=development gulp watch

(venv) % make serve
```

### Style & Lint

```zsh
(venv) % make check
(venv) % make lint

(venv) % make vet
```


## Deployment

### Publishing

E.g. Google App Engine

```zsh
: e.g. use google app engine (see https://cloud.google.com/sdk/docs/)
% cd lib
(venv) % curl -sLO https://dl.google.com/dl/cloudsdk/channels/rapid/ \
  downloads/google-cloud-sdk-<VERSION>-linux-x86_64.tar.gz

: check sha256 checksum
(venv) % echo "CHECKSUM" "" ./google-cloud-sdk-<VERSION>-linux-x86_64.tar.gz \
  | sha256sum -c -
./google-cloud-sdk-<VERSION>-linux-x86_64.tar.gz: OK
(venv) % tar zxvf google-cloud-sdk-<VERSION>-linux-x86_64.tar.gz

: setup lib/ as a root for sdk
(venv) % CLOUDSDK_ROOT_DIR=. ./google-cloud-sdk/install.sh
(venv) % cd ../

: load sdk tools
(venv) % source ./bin/load-gcloud
(venv) % gcloud init
```

```zsh
: deploy website
(venv) % source ./bin/load-gcloud
(venv) % gcloud app deploy ./app.yaml --project <project-id> --verbosity=info
```

## Testing

```zsh
(venv) % make test
(venv) % make coverage
```


## License

This project is distributed as various licenses by parts.

```txt
Lutèce
Copyright (c) 2017 Lupine Software LLC
```

### Documentation, Resource (image)

`CC-BY-NC-SA-4.0`

The files in the `static/img` directory are licensed under the
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
Public License.

[![Creative Commons License](
https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](
http://creativecommons.org/licenses/by-nc-sa/4.0/)

Check the [Legalcode](
https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode).


### Software (program)

`AGPL-3.0`

```txt
This is free software: You can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
```

See [LICENSE](LICENSE).


[pipeline]: https://gitlab.com/lupine-software/lutece/badges/master/build.svg
[coverage]: https://gitlab.com/lupine-software/lutece/badges/master/coverage.svg
[commit]: https://gitlab.com/lupine-software/lutece/commits/master
