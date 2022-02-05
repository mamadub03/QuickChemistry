"""
WSGI config for QuickChemistry project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# from django.conf import settings
#
# settings.configure(DEBUG=True)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'QuickChemistry.settings')

application = get_wsgi_application()
