"""
WSGI config for memba project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/memba")
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/site")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
print(sys.path)

application = get_wsgi_application()
