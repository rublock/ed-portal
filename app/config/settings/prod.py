import os
from .base import *

DEBUG = False

ADMINS = [
    ('Mack', 'lpsys1@gmail.com'),
]

ALLOWED_HOSTS = ['82.97.241.112']

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
