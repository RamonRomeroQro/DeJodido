"""
WSGI config for deajodido project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


#Lo que se va a poner
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deajodido.settings.development")
application = get_wsgi_application()



