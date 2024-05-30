#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py populatedatabase
daphne -b 0.0.0.0 -p $PORT webservice.asgi:application