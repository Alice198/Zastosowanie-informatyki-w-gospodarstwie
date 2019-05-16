from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('logowanie/', LoginView.as_view(), {'template_name': 'templates/login.html'}, name='Login'),
    path('rejestracja/', views.registration, name='Registration'),
    path('wylogowywanie/', views.logout_view, name='Logout'),
    path('moje_konto/', views.user_account, name='User account'),
    path('edytuj_dane/', views.edit_user, name='User edit'),
    path('zmien_haslo/', views.change_password, name='Change password'),
    path('zloz_zamownie/', views.submit_order, name='Submit order'),
    path('zloz_zamownie_wyglad/', views.submit_order_appearance, name='Submit order appearance'),
    path('zloz_zamownie_trumna/', views.submit_order_coffin, name='Submit order coffin'),
    path('zloz_zamownie_kwiaty/', views.submit_order_flower, name='Submit order flowers'),
    path('zloz_zamownie_oprawa_muzyczna/', views.submit_order_music, name='Submit order music'),
    path('podumowanie_zamowienia/', views.submit_order_summary, name='Summary submit order'),
    path('twoje_zamowienia/', views.your_order, name='Your order'),
    path('usun_konto/', views.delete_user, name='User delete'),
    path('opinie/', views.opinion, name='Opinion'),
    path('edycja_zamowienia/', views.edit_your_order, name='Edit your order'),
    path('edycja_zmarlego/', views.edit_died_from_order, name='Edit died'),
    path('edycja_trumny/', views.edit_coffin_form_order, name='Edit coffin'),
    path('edycja_kwiatow/', views.edit_flowers_form_order, name='Edit flowers'),
    path('edycja_muzyki', views.edit_music_form_order, name='Edit music'),
    path('usun_zamowienie/', views.delete_order, name='Delete order'),
]
