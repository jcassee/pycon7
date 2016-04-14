#!/usr/bin/env python

from setuptools import setup

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
        'django-cors-headers',
        'django-filter',
        'django-extensions',
        'djangorestframework',
        'LinkHeader',
        'Markdown',
        'PyYAML',
        'uritemplate.py',
    ],
)
