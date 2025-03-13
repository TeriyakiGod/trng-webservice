from django.urls import path, include
from . import views, rand_tools
from django.views.generic import TemplateView

app_name = "api"

urlpatterns = [
    path(
        "rand/int",
        views.rand_tool_view,
        {"tool": rand_tools.random_integer},
        name="rand_int",
    ),
    path(
        "rand/float",
        views.rand_tool_view,
        {"tool": rand_tools.random_float},
        name="rand_float",
    ),
    path(
        "rand/bytes",
        views.rand_tool_view,
        {"tool": rand_tools.random_bytes},
        name="rand_bytes",
    ),
    path(
        "rand/string",
        views.rand_tool_view,
        {"tool": rand_tools.random_string},
        name="rand_string",
    ),
    path(
        "rand/sequence",
        views.rand_tool_view,
        {"tool": rand_tools.random_sequence},
        name="rand_sequence",
    ),
    path(
        "rand/coin",
        views.rand_tool_view,
        {"tool": rand_tools.random_coin},
        name="rand_coin",
    ),
    path(
        "rand/dice",
        views.rand_tool_view,
        {"tool": rand_tools.random_dice},
        name="rand_dice",
    ),
    path(
        "rand/lotto",
        views.rand_tool_view,
        {"tool": rand_tools.random_lotto},
        name="rand_lotto",
    ),
    path(
        "rand/bitmap",
        views.rand_bitmap_view,
        {"tool": rand_tools.random_bitmap},
        name="rand_bitmap",
    ),
    path(
        "rand/color",
        views.rand_tool_view,
        {"tool": rand_tools.random_color},
        name="rand_color",
    ),
    path(
        "rand/bitmap/gray",
        views.rand_bitmap_view,
        {"tool": rand_tools.random_bitmap_gray},
        name="rand_bitmap_gray",
    ),
    path(
        "rand/bitmap/color",
        views.rand_bitmap_view,
        {"tool": rand_tools.random_bitmap_color},
        name="rand_bitmap_color",
    ),
    path(
        "rand/raw",
        views.rand_raw_view,
        {"tool": rand_tools.random_raw},
        name="rand_raw",
    ),
    path("insufficient_points", views.insufficient_points, name="insufficient_points"),
    path("service_unavailable", views.service_unavailable, name="service_unavailable"),
    path(
        "", TemplateView.as_view(template_name="redoc.html"), name="redoc-schema"
    ),
]
