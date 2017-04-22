from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ALLOWED_HOSTS + ['fruz.herokuapp.com',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'db', 'prod', 'db.sqlite3'),
    }
}

try:
    from .local import *
except ImportError:
    pass
