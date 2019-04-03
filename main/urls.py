from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('user_account/', views.user_account, name='user_account'),
    path('edit_user/', views.edit_user, name='edit_user'),
    path('change_password/', views.change_password, name='change_password'),

]