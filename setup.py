#!/usr/bin/env python

from distutils.core import setup

setup(
    name='pycon7',
    version='0.1',
    description='Example project for PyCon 7',
    author='Joost Cassee',
    author_email='joost@cassee.net',
    url='https://github.com/jcassee/pycon7',
    packages=['pycon7'],
    install_requires=[
        'Django',
        'django-behave',
        'django-filter',
        'django-extensions',
        'djangorestframework',
        'drf-hal-json',
        'markdown',
        'requests',
    ],
)
