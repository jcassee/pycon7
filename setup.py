#!/usr/bin/env python

from distutils.core import setup

import registronavale

setup(
    name='registronavale',
    version=registronavale.__version__,
    description='Example project for PyCon Sette',
    author='Joost Cassee',
    author_email='joost@cassee.net',
    url='https://github.com/jcassee/registronavale',
    packages=['registronavale'],
    install_requires=[
        'behave-django',
        'Django',
        'django-filter',
        'django-extensions',
        'djangorestframework',
        'drf-hal-json',
        'Markdown',
        'uritemplate.py',
    ],
)
