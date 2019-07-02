"""
WSGI config for userweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import secrets
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'userweb.settings')

print("User id:", secrets.token_urlsafe(20))

application = get_wsgi_application()
