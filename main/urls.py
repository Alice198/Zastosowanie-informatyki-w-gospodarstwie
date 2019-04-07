from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('strona_glowna/', views.home, name='Home'),
    path('logowanie/', views.login, name='Login'),
    path('rejesracja/', views.registration, name='Registration'),
    path('moje_konto/', views.user_account, name='User account'),
    path('edytuj_dane/', views.edit_user, name='User edit'),
    path('zmien_haslo/', views.change_password, name='Change password'),
    path('zloz_zamownie/', views.submit_order, name='Submit order'),
    path('twoje_zamowienia/', views.your_order, name='Your order'),
]