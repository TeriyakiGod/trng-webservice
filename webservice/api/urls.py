from django.urls import path
from .views import RandomIntView, RandomFloatView

urlpatterns = [
    path('rand/int', RandomIntView.as_view(), name='rand_int'),
    path('rand/float', RandomFloatView.as_view(), name='rand_float'),
]