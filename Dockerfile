# Взять официальный базовый образ Python с платформы Docker
FROM python:3.10.12

# Задать переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Задать рабочий каталог
WORKDIR /usr/src/app

# Установить зависимости
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Скопировать код в работчий каталог в контейнере
COPY . .