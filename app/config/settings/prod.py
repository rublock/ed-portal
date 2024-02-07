from .base import *

DEBUG = False

ADMINS = [
    ('Mack', 'lpsys1@gmail.com'),
]

ALLOWED_HOSTS = ['82.97.241.112', '127.0.0.1']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': os.environ.get('POSTGRES_DB'),
       'USER': os.environ.get('POSTGRES_USER'),
       'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
       'HOST': 'postgres',
       'PORT': 5432,
   }
}

STATIC_URL = "/static/static/"
MEDIA_URL = "/static/media/"

STATIC_ROOT = "vol/web/static"
MEDIA_ROOT = "vol/web/media"
