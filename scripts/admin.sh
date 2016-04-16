#!/bin/sh

set -e

export DJANGO_SETTINGS_MODULE=registronavale.admin-settings

python manage.py collectstatic --noinput

exec uwsgi --master \
      --http-socket=0.0.0.0:80 \
      --module=registronavale.wsgi:application \
      --static-map /static/=static/
