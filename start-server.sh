#!/usr/bin/env bash
# start-server.sh

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (python manage.py createsuperuser --no-input)
fi

if [ "x$DJANGO_MANAGEPY_MIGRATE" = 'xon' ]; then
    echo "PostgreSQL started"
    python manage.py makemigrations --noinput
    python manage.py migrate --noinput
fi


(gunicorn traffic_director_system.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"