from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ALLOWED_HOSTS + ['fruz.herokuapp.com',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd2r5al0ttce33e',
        'USER': 'kcnqsgijwlvrax',
        'PASSWORD': 'be653ac5064d5713b8b467bbf7016bddd65406345ce11c2e62843ac29df48cd4',
        'HOST': 'ec2-79-125-125-97.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',

    }
}

try:
    from .local import *
except ImportError:
    pass
