from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0']

INTERNAL_IPS = [
    '127.0.0.1',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
