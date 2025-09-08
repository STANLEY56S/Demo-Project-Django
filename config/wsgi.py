"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from common.common_utility import get_django_settings_path

# get the setting by check the prod dev
django_settings_path = get_django_settings_path()
print("django_settings_path ::: ",django_settings_path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', django_settings_path)

application = get_wsgi_application()
