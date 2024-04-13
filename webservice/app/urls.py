from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path("", views.Index.as_view(), name="Home"),
    path("forms/int", views.RandIntForm.as_view(), name="Random Integer"),
]