from .base import *

EXTERNAL_APPS = EXTERNAL_APPS + [
    'django_extensions',
]

INSTALLED_APPS = DJANGO_APPS + EXTERNAL_APPS + INTERNAL_APPS

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ALLOWED_HOSTS + ['0.0.0.0', 'localhost', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER': 'admin',
        'PASSWORD': 'adminadmin',
        'HOST': '127.0.0.1',
        'PORT': '5432',

    }
}

try:
    from .local import *
except ImportError:
    pass
