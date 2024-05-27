from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.home_page, name="index"),
    path("index", views.home_page, name="index_snd"),
    path("login", views.login_view, name="login_view"), #auth_views.LoginView.as_view(template_name='login.html')
    path("logout", views.logout_view, name="logout_view"),
    path("change_user", views.change_user, name="change_user"),
    path("signup", views.signup, name="signup"),
    path('choose_booking/booking/<str:transport>/<str:travel_type>/', views.booking, name='booking'),
    path("check_booking", views.check_page, name="check_booking"),
    path("cancel_booking", views.cancel_page, name="cancel_booking"),
    path("choose_booking", views.choose_booking, name="choose_booking"),
    path('process_payment/<int:ticket_id>/', views.process_payment, name='process_payment'),
    path('payment_done/<str:token>/', views.payment_done, name='payment_done'),
]
