#!/usr/bin/make

install:
	@virtualenv -p python3 venv
	@venv/bin/pip install -r requirements.txt
	@venv/bin/pip install -r requirements.dev.txt

flake8:
	@venv/bin/flake8 product api

pylint:
	@venv/bin/pylint --load-plugins pylint_django product api

lint: flake8 pylint

unit_test:
	@venv/bin/python manage.py test

test: lint unit_test