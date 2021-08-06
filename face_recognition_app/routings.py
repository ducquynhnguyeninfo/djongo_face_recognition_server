## game/routing.py
from django.conf.urls import url
from face_recognition_app.face_consumer import FaceConsumer

websocket_urlpatterns = [
    url(r'^ws/play/(?P<room_code>\w+)/$', FaceConsumer.as_asgi()),
]
