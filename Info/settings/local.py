from .base import *

SECRET_KEY = 'django-insecure-&)u3+!=r%t7^c774^7(r6&=$v=iq3k1hnv*6i8d$3n=1t46df*'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}