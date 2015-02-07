#!/usr/bin/env python
import os
import sys
import socket

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(BASE_DIR)

if __name__ == "__main__":
    if socket.gethostname() == "srv-prod-web-03":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings.production")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)