from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path("", views.index, name="Home"),
    path("forms/int", views.rand_int_form, name="Random integer"),
    path("about", views.about, name="About"),
]