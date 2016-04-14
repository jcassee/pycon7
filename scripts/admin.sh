#!/bin/sh

set -e

python manage.py collectstatic --noinput

uwsgi --master \
      --http-socket=0.0.0.0:80 \
      --module=registronavale.admin-wsgi:application \
      --static-map /static/=static/
