from django import views
from django.urls import path
from . import views



urlpatterns = [
    path('sandwich/', views.my_index, name='home'),
    path('login/', views.my_login, name='login'),
    path('signup/', views.my_signup, name='signup'),
]