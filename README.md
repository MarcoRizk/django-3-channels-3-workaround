# django-channels-3-workaround

[![Build Status](https://travis-ci.org/MarcoRizk/django-channels-3-workaround.svg?branch=master)](https://travis-ci.org/MarcoRizk/django-channels-3-workaround)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Describes ae issue with limited number of requests handling for django 3 and channels 3. Check out the project's [documentation](http://MarcoRizk.github.io/django-channels-3-workaround/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```
