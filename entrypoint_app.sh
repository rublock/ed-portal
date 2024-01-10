#!/usr/bin/env sh

python app/manage.py migrate --noinput
python app/manage.py loaddata 001_news 002_courses 003_lessons ./app/mainapp/fixtures/004_teachers.json
python app/manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'lpsys1@gmail.com', 'admin')"
python app/manage.py runserver 0.0.0.0:8000