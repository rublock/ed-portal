# Взять официальный базовый образ Python с платформы Docker
FROM python:3.10.12

# Задать переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Задать рабочий каталог
WORKDIR /code

# Установить зависимости
RUN apt update && \
    apt-get install -y build-essential
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD ["uwsgi", "--master", "--ini", "/config/uwsgi/uwsgi.ini"]

# Скопировать код в работчий каталог в контейнере
COPY . .
