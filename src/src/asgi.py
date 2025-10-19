"""
ASGI config for src project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from .settings import base
from django.core.asgi import get_asgi_application

if base.DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings.dev")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings.prod")

application = get_asgi_application()
