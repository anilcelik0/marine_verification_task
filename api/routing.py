
from django.urls import path
from . import consumer

websocket_urlpatterns = [
    path('ws/token/', consumer.TokenConsumer.as_asgi()),
]