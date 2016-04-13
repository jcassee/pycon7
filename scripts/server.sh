#!/bin/sh

set -e

python manage.py migrate --noinput

uwsgi --master --http-socket=0.0.0.0:80 --module=registronavale.wsgi:application
