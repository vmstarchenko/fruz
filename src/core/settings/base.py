"""
Django settings for fruz project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(CORE_DIR, ...)
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # config dir
PROJECT_DIR = os.path.dirname(CORE_DIR) # src dir
BASE_DIR = os.path.dirname(PROJECT_DIR) # project root dir

# Append folders to path
sys.path.insert(0, os.path.join(CORE_DIR))
sys.path.insert(0, os.path.join(PROJECT_DIR))
sys.path.insert(0, os.path.join(BASE_DIR))
sys.path.insert(0, os.path.join(PROJECT_DIR, 'lib'))
sys.path.insert(0, os.path.join(PROJECT_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')!4mpnra51^lr7zo#8$%@q-5$980#-!0x5*a7&825sau+nk@%k'

ALLOWED_HOSTS = []

# Application definition
VERSION = '2'


DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

EXTERNAL_APPS = [
    'solo'
]

INTERNAL_APPS = [
    'schedule'
]

INSTALLED_APPS = DJANGO_APPS + EXTERNAL_APPS + INTERNAL_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'src.core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Auth
# LOGIN_URL = "/login/"
# LOGIN_REDIRECT_URL = "/"
# AUTH_USER_MODEL = 'apps.user'

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(PROJECT_DIR, 'locale'),
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/%s/' %VERSION

STATIC_ROOT = os.path.join(BASE_DIR, 'var', 'www', VERSION)

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]
