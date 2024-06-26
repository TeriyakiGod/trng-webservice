from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'auth'

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("account/", views.AccountView.as_view(), name="account"),
]

