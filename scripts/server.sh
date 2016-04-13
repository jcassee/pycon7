#!/bin/sh

set -e

python manage.py migrate --noinput
python manage.py loaddata initial_data.yml

uwsgi --master --http-socket=0.0.0.0:80 --module=registronavale.wsgi:application
