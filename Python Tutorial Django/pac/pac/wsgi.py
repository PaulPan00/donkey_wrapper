# Create by Packetsss
# Personal use is allowed
# Commercial use is prohibited

"""
WSGI config for pac project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pac.settings')

application = get_wsgi_application()
