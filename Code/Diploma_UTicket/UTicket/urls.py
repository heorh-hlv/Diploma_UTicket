from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="index"),
    path("index", views.home_page, name="index_snd"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("booking", views.booking_page, name="booking"),
    path("check_booking", views.check_page, name="check_booking"),
    path("cancel_booking", views.cancel_page, name="cancel_booking"),
]
