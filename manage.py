#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv


def main():
    """Run administrative tasks."""
    from common.common_utility import get_django_settings_path
    BASE_DIR = Path(__file__).resolve().parent.parent

    # load .env file
    load_dotenv(BASE_DIR / ".env")

    # get the setting by check the prod dev
    django_settings_path = get_django_settings_path()

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', django_settings_path)
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
