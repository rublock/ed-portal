#Взять официальный базовый образ Python с платформы Docker
FROM python:3.12.0-alpine

#Задать переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Задать рабочий каталог
WORKDIR /code

#Установить зависимости
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY app /code/