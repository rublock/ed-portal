#!/bin/sh

set -e

ls -la /vol/
ls -la /vol/web

whoami

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py loaddata 001_news 002_courses 003_lessons ./mainapp/fixtures/004_teachers.json

uwsgi --socket :9000 --workers 4 --master --enable-threads --module config.wsgi