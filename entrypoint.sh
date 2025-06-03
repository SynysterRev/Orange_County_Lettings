#!/bin/sh
# Exit on error
set -o errexit

# Apply any outstanding database migrations
python manage.py migrate

exec gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000