#!/bin/bash

function __sepr () {
    printf '# ----------------------------------------------------------\n'
}

__sepr
cat /etc/os-release

__sepr
bash --version

__sepr
python -V

__sepr
pip -V

__sepr
mkdir -pv public_collect_static
mkdir -pv public

__sepr
pip list
# pip install -r aaa/deps/pip/prod.pip

__sepr
python manage.py check

#$(python) manage.py collectstatic --noinput \
#    --settings aaa.settings.prod \
#    --ignore admin \
#    --ignore django_non_dark_admin

#$(python) manage.py distill-local --force \
#    --settings aaa.settings.prod