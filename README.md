## Образовательный портал

## Стек

- Python > 3.7
  - isort, black, autoflake
  - Django < 3.3
  - Celery[Redis]
- PostgreSQL 14

#### Чтобы активировать логи на сервере
```bash
docker logs -f [имя_контейнера] &> /app/var/log/main_log.log &
```
