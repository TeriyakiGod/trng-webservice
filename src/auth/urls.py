from django.urls import path
from . import views


app_name = 'auth'

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("account/", views.AccountView.as_view(), name="account"),
    path("verify/", views.verify_email, name="verify"),
    path("check-email/", views.check_email, name="check-email"),
    path("change-password/", views.ChangePasswordView.as_view(), name="change-password"),
]

