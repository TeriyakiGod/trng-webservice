#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
daphne -b 0.0.0.0 -p 8003 webservice.asgi:application