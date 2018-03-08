from .base_settings import *


ALLOWED_HOSTS = ["*"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'enigmacast',
        'USER': 'enigma',
        'PASSWORD': 'volatile',
        'HOST': 'localhost',
        'PORT': '',
    }
}