# Rogue Trader

## Intro
{{ TODO }}

## The Build

The build runs off of a [Docker][] configuration for a Django-based web application.

- The [Django][] application is served by [Gunicorn][] (WSGI application).
- [NginX][] is the reverse proxy & static file server. Static and media files are
  persistently stored in volumes.
- [Python][] dependencies are managed through [pipenv][], with `Pipfile` and `Pipfile.lock`.
- We use [ReactJS][] on the front-end through a dedicated Node-based container.
- Tests are run using [tox][], [pytest][], and other tools such as [safety][], [bandit][], [isort][] and [prospector][].

## Makefile
A fairly extensive [Makefile][] is available for convenience. You might need to use `sudo make`
instead of just `make` because the `docker` and `docker-compose` commands sometimes need
admin rights.

The syntax looks like `make <command>` (without the braces). A full list of commands can be found
within the Makefile itself.

## Requirements
You'll need to install [Docker][] and [Docker-Compose][] before the system will work.

## Getting the system running

The simplest way to get this stack of containers working is to use the commands in the
included Makefile, which will do everything for you. 

The workflow should be as simple as:

* First, build everything: `make build` (This will build everything and start
all of the containers)
* Then, run the first load - which will migrate the database, create a Django admin 
user, and prompt you for a password for that user: `make firstload`
* Then, you can load the system with data, through attached fixtures - 
you'll just need to specify which apps you want to load, for example:
`make loaddata APP=stocks`
* You should then be able to visit http://127.0.0.1:8000/admin/, log in with the
name 'admin' and the password you specified - and then you'll have access to 
the backend.
* The system runs on a main, scheduled Celery Beat task. The build process
does not start this task automatically and you can easily start it manually with
`make startbeat`. This will immediately start processing the data that you have
previously loaded (and it will probably fail if the database is empty).
* If your static files haven't loaded for some unknown reason (everything is 
unstyled, or missing CSS, just run `make collectstatic`, which will fix it for you.

#### Note:
There are a lot of Make utilities in the Makefile that will cover pretty much
all of the regular Django manage.py developmental workflow stuff you need. It's
written as a simple wrapper around the regular `docker exec` style commands - 
but it will save you a lot of typing, so take a look at that for some 
very handy shortcuts.

### Alternatively, regular Docker
Alternatively, if you prefer the more traditional Docker commands, you can 
just manually use the regular commands, for example:

* `docker-compose build` or `make build`.
* `docker-compose run --rm djangoapp roguetrader/manage.py migrate`
* `docker-compose run --rm djangoapp hello/manage.py collectstatic --no-input'`

(You'll need to create admin users the same way.)

## Running the tests
To run the full test suite, simply run:

- `make runtests`

(This will both install the test suite and run it all.)

Other test utilities are also available:

- `make checksafety` (Checks for security holes or pre-deploy issues.)
- `make checkstyle` (Checks for code style.)
- `make coverage` (Reports code coverage.)

## Predeploy
Before deploying, you can run a `clean` as well as the testsuite by running:

- `make predeploy`

This should give you an actionable list of things to take care of before
redeploying.

[Docker]: https://www.docker.com/
[Django]: https://www.djangoproject.com/
[Gunicorn]: http://gunicorn.org/
[NginX]: https://www.nginx.com/
[Postgres]: https://www.postgresql.org/
[Python]: https://www.python.org/
[pipenv]: https://docs.pipenv.org/
[tox]: https://tox.readthedocs.io/en/latest/
[pytest]: https://docs.pytest.org/en/latest/
[safety]: https://pyup.io/safety/
[bandit]: https://github.com/openstack/bandit
[isort]: https://github.com/timothycrosley/isort
[prospector]: https://github.com/landscapeio/prospector
[GitLab]: https://about.gitlab.com/
[ReactJS]: https://reactjs.org/
[Makefile]: https://www.gnu.org/software/make/manual/make.html
[Docker-Compose]: https://docs.docker.com/compose/
