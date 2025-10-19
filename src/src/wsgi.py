"""
WSGI config for src project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from .settings import base
from django.core.wsgi import get_wsgi_application

if base.DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings.dev")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings.prod")

application = get_wsgi_application()
