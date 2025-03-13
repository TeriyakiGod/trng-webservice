from django.urls import path
from . import views
from api import rand_tools
app_name = 'webapp'

urlpatterns = [
    path("", views.template_view, name="index", kwargs={"template": "index.html"}),
    path("about/", views.template_view, name="about", kwargs={"template": "about.html"}),
    path("contact/", views.template_view, name="contact", kwargs={"template": "contact.html"}),
    path("rand-int-form/", views.random_tool_form_view, name="rand_int", kwargs={"tool": rand_tools.random_integer}),
    path("rand-float-form/", views.random_tool_form_view, name="rand_float", kwargs={"tool": rand_tools.random_float}),
    path("rand-string-form/", views.random_tool_form_view, name="rand_string", kwargs={"tool": rand_tools.random_string}),
    path("rand-bytes-form/", views.random_tool_form_view, name="rand_bytes", kwargs={"tool": rand_tools.random_bytes}),
    path("rand-sequence-form/", views.random_tool_form_view, name="rand_sequence", kwargs={"tool": rand_tools.random_sequence}),
    path("rand-coin-form/", views.random_tool_form_view, name="rand_coin", kwargs={"tool": rand_tools.random_coin}),
    path("rand-dice-form/", views.random_tool_form_view, name="rand_dice", kwargs={"tool": rand_tools.random_dice}), 
    path("rand-lotto-form/", views.random_tool_form_view, name="rand_lotto", kwargs={"tool": rand_tools.random_lotto}),
    path("rand-bitmap-form/", views.random_tool_form_view, name="rand_bitmap", kwargs={"tool": rand_tools.random_bitmap}),
    path('rand-bitmap-gray-form/', views.random_tool_form_view, name='rand_bitmap_gray', kwargs={"tool": rand_tools.random_bitmap_gray}),
    path('rand-bitmap-color-form/', views.random_tool_form_view, name='rand_bitmap_color', kwargs={"tool": rand_tools.random_bitmap_color}),
    path('rand-raw-form/', views.random_tool_form_view, name='rand_raw', kwargs={"tool": rand_tools.random_raw}),
    path("rand-color-form/", views.random_tool_form_view, name="rand_color", kwargs={"tool": rand_tools.random_color}),
    path("privacy-policy/", views.template_view, name="privacy_policy", kwargs={"template": "privacy_policy.html"}),
    path("terms-of-service/", views.template_view, name="terms_of_service", kwargs={"template": "tos.html"}),
]

