"""
WSGI config for deajodido project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Viejo por si la cago
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deajodido.settings")

import os


if os.path.isfile ('/etc/secret_key.txt'):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deajodido.settings.production")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deajodido.settings.development")
print(os.environ['DJANGO_SETTINGS_MODULE'])

application = get_wsgi_application()





