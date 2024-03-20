from django.urls import path
from .views import RandomIntView, RandomFloatView, RandomBytesView, TestView

urlpatterns = [
    path('rand/int', RandomIntView.as_view(), name='rand_int'),
    path('rand/float', RandomFloatView.as_view(), name='rand_float'),
    path('rand/bytes', RandomBytesView.as_view(), name='rand_bytes'),
    path('test', TestView.as_view(), name='test'),
]