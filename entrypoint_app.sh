#!/usr/bin/env sh

python app/manage.py migrate --noinput
python app/manage.py loaddata 001_news 002_courses 003_lessons ./app/mainapp/fixtures/004_teachers.json
python app/manage.py runserver 0.0.0.0:8000