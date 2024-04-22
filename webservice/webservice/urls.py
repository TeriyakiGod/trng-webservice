from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", include("app.urls", namespace="app"), name="app"),
    path("api/", include("api.urls", namespace="api"), name="api"),
    path("auth/", include("auth.urls", namespace="auth"), name="auth"),
]
