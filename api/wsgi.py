"""
WSGI config for api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(BASE_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'api.settings.production'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()