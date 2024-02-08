from .base import *

DEBUG = False

ADMINS = [
    ('rublock', 'lpsys1@gmail.com'),
]

ALLOWED_HOSTS = ['213.171.8.9',]

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

STATIC_URL = '/static/static/'
MEDIA_URL = '/static/media/'

MEDIA_ROOT = '/vol/web/media'
STATIC_ROOT = '/vol/web/static'
