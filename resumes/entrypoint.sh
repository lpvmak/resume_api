#! /bin/sh
python manage.py migrate;
python manage.py collectstatic --noinput
gunicorn resumes.wsgi --bind 0.0.0.0:8000