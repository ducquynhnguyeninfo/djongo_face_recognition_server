"""
ASGI config for djongo_face_recognition_server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import face_recognition_app.routings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djongo_face_recognition_server.settings')
django.setup()

# application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            face_recognition_app.routings.websocket_urlpatterns
        )
    ),
    ## IMPORTANT::Just HTTP for now. (We can add other protocols later.)
})
