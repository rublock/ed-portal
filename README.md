## Learning management system

`Python 3.10` `Django 4.2.7` `PostgreSQL 14` `Celery` `Redis` `Django TestCase` `Selenium` `locust` `Docker` `Nginx` `UWSGI`

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
```angular2html
docker compose -f docker-compose-prod.yml up
```
> главная страница
![](https://raw.githubusercontent.com/rublock/ed_portal/main/app/static/img/main_page.PNG)
> логи
![](https://raw.githubusercontent.com/rublock/ed_portal/main/app/static/img/logs.PNG)
> API
![](https://raw.githubusercontent.com/rublock/ed_portal/main/app/static/img/api.PNG)
> redoc
![](https://raw.githubusercontent.com/rublock/ed_portal/main/app/static/img/redoc.PNG)
> swagger
![](https://raw.githubusercontent.com/rublock/ed_portal/main/app/static/img/swagger.PNG)
> личный кабинет
![](https://raw.githubusercontent.com/rublock/ed_portal/main/app/static/img/profile.PNG)
> debug toolbar
![](https://raw.githubusercontent.com/rublock/ed_portal/main/app/static/img/toolbar.PNG)
