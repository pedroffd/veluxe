#!/bin/sh

# Stop on error
set -e

echo "Apply Database Migrations..."
python manage.py migrate

exec "$@"
