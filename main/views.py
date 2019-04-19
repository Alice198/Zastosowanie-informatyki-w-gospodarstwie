# Create your views here.

from django.shortcuts import render


def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def registration(request):
    return render(request, 'registration.html')


def user_account(request):
    return render(request, 'user_account.html')


def edit_user(request):
    return render(request, 'edit_user.html')


def change_password(request):
    return render(request, 'change_password.html')
