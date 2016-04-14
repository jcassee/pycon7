"""
Django settings for the registronavale project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0y12s%wbyr)sg_2jh4d4!084siatq7yb3iajs1=zwq(geybbdj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',

    'corsheaders',
    'django_extensions',
    'behave_django',
    'rest_framework',

    'ship_registry',
]

MIDDLEWARE_CLASSES = [
    'corsheaders.middleware.CorsMiddleware',
]
ROOT_URLCONF = 'registronavale.urls'
APPEND_SLASH = False

WSGI_APPLICATION = 'registronavale.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'drf_hal.renderers.HalRenderer',
    ],
    'EXCEPTION_HANDLER': 'drf_hal.vnderror_exception_handler',
}

TIME_ZONE = 'Europe/Amsterdam'
USE_TZ = True
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True

STATIC_URL = '/static/'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


# Disable deprecation warnings
import logging

def filter_deprecation_warnings(record):
    warnings_to_suppress = [
        'RemovedInDjango110Warning'
    ]
    # Return false to suppress message.
    return not any([warn in record.getMessage()
                    for warn in warnings_to_suppress])

warn_logger = logging.getLogger('py.warnings')
warn_logger.addFilter(filter_deprecation_warnings)


# Include local config
try:
    from local_settings import *
except ImportError:
    pass
