#!/bin/sh

set -e

basedir=`dirname "$0"`
cd "$basedir/.."

python manage.py syncdb --noinput
python manage.py migrate --noinput

uwsgi --master --http-socket=0.0.0.0:80 --home=. --module=wsgi:application --uid=nobody
