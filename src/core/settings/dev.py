from .base import *

EXTERNAL_APPS = EXTERNAL_APPS + [
    'django_extensions',
]

INSTALLED_APPS = DJANGO_APPS + EXTERNAL_APPS + INTERNAL_APPS

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'var', 'db', 'dev', 'db.sqlite3'),
    }
}

try:
    from .local import *
except ImportError:
    pass
