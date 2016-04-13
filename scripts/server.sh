#!/bin/sh

set -e

python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py loaddata initial_data.yaml

uwsgi --master \
      --http-socket=0.0.0.0:80 \
      --module=registronavale.wsgi:application \
      --static-map /static/=static/
