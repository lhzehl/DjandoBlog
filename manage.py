#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
"""
 for create new app in (venv) ---> python manage.py startapp blog
 for migrate db     in venv ---> python manage.py makemigrations --->python manage.py migrate
"""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoBlog.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
