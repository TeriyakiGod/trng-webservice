from django.urls import path
from .views import RandomNumberView

urlpatterns = [
    path('rand/int', RandomNumberView.as_view(), name='random_numbers'),
]