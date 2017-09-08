# Lutèce

`/lytɛs/`

[![build status](https://gitlab.com/lupine-software/lutece/badges/master/build.svg)](https://gitlab.com/lupine-software/lutece/commits/master)

![Lupine Software LLC](https://gitlab.com/lupine-software/lutece/raw/master/static/img/lupine-software-logo-300x300.png)

```txt
Lutèce; LUpine sofTwarE website to introduCE about our product and ourselves
```

The website of [Lupine Software](https://lupine-software.com).


## Requirements

* Python `3.5` (or `2.7`)


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

### Dependencies

TODO


## Development

```zsh
(venv) % python main.py
```

### Style & Lint

```zsh
(venv) % pip install pylint flake8
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
(venv) % echo "<CHECKSUM>" "" ./google-cloud-sdk-<VERSION>-linux-x86_64.tar.gz \
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

TODO


## License

Lutèce; Copyright (c) 2017 Lupine Software LLC

### Software

This is free software;  
You can redistribute it and/or modify it under the terms of
the GNU Affero General Public License (AGPL).

See `LICENSE`.

### Documentation, content and images

[![Creative Commons License](
https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](
http://creativecommons.org/licenses/by-nc-sa/4.0/)  
This work is licensed under a [
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

See [Legalcode](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)
