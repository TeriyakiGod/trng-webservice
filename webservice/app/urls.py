from django.urls import path
from . import views


app_name = 'app'

urlpatterns = [
    path("", views.display_page, name="index", kwargs={"template": "index.html"}),
    path("about/", views.display_page, name="about", kwargs={"template": "about.html"}),
    path("contact/", views.display_page, name="contact", kwargs={"template": "contact.html"}),
    path("rand_int/", views.display_page, name="rand_int", kwargs={"template": "forms/rand_int.html"}),
    path("rand_float/", views.display_page, name="rand_float", kwargs={"template": "forms/rand_float.html"}),
    path("rand_string/", views.display_page, name="rand_string", kwargs={"template": "forms/rand_string.html"}),
    path("rand_bytes/", views.display_page, name="rand_bytes", kwargs={"template": "forms/rand_bytes.html"}),
    path("rand_sequence/", views.display_page, name="rand_sequence", kwargs={"template": "forms/rand_sequence.html"}),
    path("rand_coin/", views.display_page, name="rand_coin", kwargs={"template": "forms/rand_coin.html"}),
    path("rand_dice/", views.display_page, name="rand_dice", kwargs={"template": "forms/rand_dice.html"}),
    path("rand_lotto/", views.display_page, name="rand_lotto", kwargs={"template": "forms/rand_lotto.html"}),
]

