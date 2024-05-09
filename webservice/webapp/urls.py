from django.urls import path
from . import views
from api import rand_tools

app_name = 'webapp'

urlpatterns = [
    path("", views.template_view, name="index", kwargs={"template": "index.html"}),
    path("about/", views.template_view, name="about", kwargs={"template": "about.html"}),
    path("contact/", views.template_view, name="contact", kwargs={"template": "contact.html"}),
    path("rand_int/", views.random_tool_form_view, name="rand_int", kwargs={"tool": rand_tools.random_integer}),
    path("rand_float/", views.random_tool_form_view, name="rand_float", kwargs={"tool": rand_tools.random_float}),
    path("rand_string/", views.random_tool_form_view, name="rand_string", kwargs={"tool": rand_tools.random_string}),
    path("rand_bytes/", views.random_tool_form_view, name="rand_bytes", kwargs={"tool": rand_tools.random_bytes}),
    path("rand_sequence/", views.random_tool_form_view, name="rand_sequence", kwargs={"tool": rand_tools.random_sequence}),
    path("rand_coin/", views.random_tool_form_view, name="rand_coin", kwargs={"tool": rand_tools.random_coin}),
    path("rand_dice/", views.random_tool_form_view, name="rand_dice", kwargs={"tool": rand_tools.random_dice}), 
    path("rand_lotto/", views.random_tool_form_view, name="rand_lotto", kwargs={"tool": rand_tools.random_lotto}),
    path("rand_bitmap/", views.random_tool_form_view, name="rand_bitmap", kwargs={"tool": rand_tools.random_bitmap})
]

