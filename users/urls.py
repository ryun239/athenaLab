from django import views
from django.urls import path
from . import views



urlpatterns = [
    path('login/', views.my_login),
    path('signup/', views.my_signup),
]