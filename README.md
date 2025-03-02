## Learning management system
портал для размещения образовательных программ

#### WEB http://188.225.37.37/

`Python 3.10` `Django 4.2.7` `DRF` `Swagger` `Redoc` `PostgreSQL 14` `Celery` `Redis` `Django TestCase` `Selenium` 
`locust` `Docker` `Nginx` `UWSGI`

* запуск без контейнера для тестов
```commandline
pip install -r requirements.txt
```
```commandline
python manage.py migrate
```
```commandline
python manage.py loaddata 001_news 002_courses 003_lessons ./mainapp/fixtures/004_teachers.json
```
```commandline
python manage.py runserver
```
* тестирование
```angular2html
python manage.py test
```
* нагрузочное тестирование
```angular2html
locust
```
![](https://raw.githubusercontent.com/rublock/ed_portal/main/app/static/img/locust.PNG)

#### Deploy
* переименуйте .env.sample в .env и заполните
* установите docker на вашем сервере
```html
docker compose -f docker-compose-prod.yml up
```
* главная страница
![](https://raw.githubusercontent.com/rublock/ed_portal/main/app/static/img/main_page.PNG)
* логи
![](https://raw.githubusercontent.com/rublock/ed_portal/main/app/static/img/logs.PNG)
* личный кабинет
![](https://raw.githubusercontent.com/rublock/ed_portal/main/app/static/img/profile.PNG)
* debug toolbar
![](https://raw.githubusercontent.com/rublock/ed_portal/main/app/static/img/toolbar.PNG)
* API
![](https://github.com/rublock/ed_portal/blob/main/app/static/img/api.png)
* Redoc
![](https://github.com/rublock/ed_portal/blob/main/app/static/img/redoc.png)
* Swagger
![](https://github.com/rublock/ed_portal/blob/main/app/static/img/swagger.png)
