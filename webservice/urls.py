from django.contrib import admin
from django.urls import path, include
from trng.views import ws_status
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", include("webapp.urls", namespace="app"), name="app"),
    path("api/", include("api.urls", namespace="api"), name="api"),
    path("auth/", include("auth.urls", namespace="auth"), name="auth"),
    path("status/", ws_status, name="status"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)