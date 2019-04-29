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
    path('zloz_zamownie_wygląd/', views.submit_order_appearance, name='Submit order appearance'),
    path('zloz_zamownie_trumna/', views.submit_order_coffin, name='Submit order coffin'),
    path('zloz_zamownie_kwiaty/', views.submit_order_flower, name='Submit order flowers'),
    path('zloz_zamownie_muzyk/', views.submit_order_music, name='Submit order music'),
    path('podumowanie_zamówienia/', views.submit_order_summary, name='Summary submit order'),
    path('twoje_zamowienia/', views.your_order, name='Your order'),
    path('usun_konto/', views.delete_user, name='User delete'),
]
