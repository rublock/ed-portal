## Пэт проект - образовательный портал

`Python 3.10` `Django 4.2.7` `PostgreSQL 14` `Celery` `Redis` `Django TestCase` `Selenium` `locust` `Docker` `Nginx` `UWSGI`

* тестирование
```angular2html
python manage.py test
```
* нагрузочное тестирование
```angular2html
locust
```
![](C:\git\ed_portal\app\static\img\locust.PNG)

#### Deploy
* переименуйте .env.sample в .env и заполните
* установите docker на вашем сервере
```angular2html
docker compose -f docker-compose-prod.yml up
```
> главная страница
![](C:\git\ed_portal\app\static\img\main_page.PNG)
> логи
![](C:\git\ed_portal\app\static\img\logs.PNG)
> личный кабинет
![](C:\git\ed_portal\app\static\img\profile.PNG)
> debug toolbar
![](C:\git\ed_portal\app\static\img\toolbar.PNG)
