#!/bin/bash

python manage.py makemigrations webapp trng --noinput
python manage.py migrate --noinput
python manage.py populatedatabase
python manage.py collectstatic --noinput
daphne -b 0.0.0.0 -p $PORT webservice.asgi:application