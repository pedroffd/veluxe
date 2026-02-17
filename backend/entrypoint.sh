#!/bin/sh

# Stop on error
set -e

echo "Collect Static Files..."
python manage.py collectstatic --no-input

echo "Apply Database Migrations..."
python manage.py migrate

exec "$@"
