#!/bin/bash
export DJANGO_SETTINGS_MODULE=webservice.settings
python manage.py migrate --noinput
python manage.py populatedatabase
python manage.py collectstatic --noinput
daphne -b 0.0.0.0 -p $TRNG_WEBSERVICE_PORT webservice.asgi:application