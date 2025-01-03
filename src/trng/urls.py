from django.urls import path

from .consumers import TrngConsumer

urlpatterns = [
    path('ws', TrngConsumer.as_asgi()),
]