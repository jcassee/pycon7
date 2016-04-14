"""
Django settings for the registronavale project.
"""

from registronavale.settings import *

MIDDLEWARE_CLASSES += [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

INSTALLED_APPS += [
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
            ],
            'debug': True,
        }
    },
]

ROOT_URLCONF = 'registronavale.admin-urls'

CORS_ORIGIN_ALLOW_ALL = False
