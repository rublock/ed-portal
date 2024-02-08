# Взять официальный базовый образ Python с платформы Docker
FROM python:alpine3.19

# Задать переменные среды
ENV PYTHONUNBUFFERED 1

# Скопировать код в работчий каталог в образ
COPY ./requirements.txt ./requirements.txt
COPY ./app /app
COPY ./scripts /scripts
COPY ./app/static /vol/web/static

# Задать рабочий каталог
WORKDIR /app
EXPOSE 8000

# Установка python, venv, зависимостей, регистарция пользователя,
# драйвер postgres (до зависимостей), папки для статики с разрешениями
RUN python -m venv /python && \
    /python/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    /python/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home admin && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R admin:admin /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

# Путь к локальному окружению
ENV PATH="/scripts:/python/bin:$PATH"

# Переключаемся на локального пользователя
USER admin

CMD ["run.sh"]