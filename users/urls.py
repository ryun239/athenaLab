from unicodedata import name
from django import views
from django.urls import path
from . import views



urlpatterns = [
    path('', views.my_index, name='home'),
    path('sandwich/', views.my_index, name='home'),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('signup/', views.my_signup, name='signup'),
]