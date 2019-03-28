# Create your views here.

from django.shortcuts import render


def base(request):
    return render (request, 'base.html')


def home(request):
    return render (request, 'home.html')


def login(request):
    return render (request, 'login.html')


def registration(request):
    return render (request, 'registration.html')

