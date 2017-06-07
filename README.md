# Lutece

`//`


```txt
Lutuce; ...
```

The team website of [Lupine Software](https://team.lupine-software.com).


## Requirements

* Python `3.5`

## Setup

```zsh
: python
: setup venv as you like (e.g. use nodeenv on Gentoo Linux)
% sudo emerge -av virtualenv (or just `sudo pip install virtualenv`)

% python3.5 -m venv venv
% source venv/bin/activate
(venv) % python -V
3.5

(venv) % pip install --upgrade pip setuptools
(venv) % pip install -r requirements.txt
```


## Development

### Serve

```zsh
% python main.py
```


## Release

### Prepare production environment

At first, setup for production environment.

```zsh
: e.g. use google app engine
(venv) % curl -sLO https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-157.0.0-linux-x86_64.tar.gz

: check sha256 checksum
(venv) % sha256sum google-cloud-sdk-157.0.0-linux-x86_64.tar.gz
95b98fc696f38cd8b219b4ee9828737081f2b5b3bd07a3879b7b2a6a5349a73f  google-cloud-sdk-157.0.0-linux-x86_64.tar.gz

(venv) % tar zxvf google-cloud-sdk-157.0.0-linux-x86_64.tar.gz

: we don\'t install this global environment even if development
(venv) % CLOUDSDK_ROOT_DIR=. ./google-cloud-sdk/install.sh

: load sdk tools
(venv) % source ./bin/load-gcloud
(venv) % gcloud init
```

### Deployment

Publish

```zsh
: deploy website
(env) % ./bin/load-gcloud && gcloud app deploy ./app.yaml --project <project-id> --verbosity=info
```


## License

Lutece; Copyright (c) 2017 Lupine Software, LLC

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
