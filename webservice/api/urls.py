from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views, rand_tools
app_name = 'api'

urlpatterns = [
    path('rand/int', views.rand_tool_view, {"tool": rand_tools.random_integer}, name='rand_int'),
    path('rand/float', views.rand_tool_view, {"tool": rand_tools.random_float}, name='rand_float'),
    path('rand/bytes', views.rand_tool_view, {"tool": rand_tools.random_bytes}, name='rand_bytes'),
    path('rand/string', views.rand_tool_view, {"tool": rand_tools.random_string}, name='rand_string'),
    path('rand/sequence', views.rand_tool_view, {"tool": rand_tools.random_sequence}, name='rand_sequence'),
    path('rand/coin', views.rand_tool_view, {"tool": rand_tools.random_coin}, name='rand_coin'),
    path('rand/dice', views.rand_tool_view, {"tool": rand_tools.random_dice}, name='rand_dice'),
    path('rand/lotto', views.rand_tool_view, {"tool": rand_tools.random_lotto}, name='rand_lotto'),
    path('rand/bitmap', views.rand_bitmap_view, name='rand_bitmap'),
    path('rand/color', views.rand_tool_view, {"tool": rand_tools.random_color}, name='rand_color'),
    
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='api:schema'), name='swagger-ui'),
]