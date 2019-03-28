from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
]