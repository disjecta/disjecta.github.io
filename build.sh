#!/bin/bash

function __sepr () {
    printf '# ----------------------------------------------------------\n'
}

function __diagnostics () {

    __sepr
    cat /etc/os-release

    __sepr
    bash --version

    __sepr
    which python
    which python3

    __sepr
    which pip
    which pip3

    __sepr
    which pipenv

    __sepr
    python -V

    __sepr
    python3 -V

    __sepr
    pip -V

    __sepr
    pip install --upgrade pip

    __sepr
    pip list
}

__diagnostics

__sepr
pip install -r aaa/deps/pip/prod.pip

# __sepr
# python manage.py check

__sepr
mkdir -pv public_collect_static
mkdir -pv public

__sepr
python3 manage.py collectstatic --noinput \
    --settings aaa.settings.prod \
    --ignore admin \
    --ignore django_non_dark_admin

__sepr
python3 manage.py distill-local --force \
    --settings aaa.settings.prod
