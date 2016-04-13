#!/bin/sh

set -e

pip install -r requirements.txt
python manage.py behave
