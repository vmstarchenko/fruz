from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ALLOWED_HOSTS + ['fruz.herokuapp.com',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER': 'admin_me',
        'PASSWORD': 'adminadminquerty',
        'HOST': 'fruz.herokuapp.com',
        'PORT': '5432',

    }
}

try:
    from .local import *
except ImportError:
    pass
