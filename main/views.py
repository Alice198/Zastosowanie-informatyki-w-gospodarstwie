# Create your views here.
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'home.html')


# def login(request):
#     return render(request, 'login.html')


def registration(request):
    """Register for new users"""
    if request.method != 'POST':
        form = UserCreationForm()   # Empty form to register
    else:
        form = UserCreationForm(data=request.POST)  # Fill form to register
        if form.is_valid():
            new_user = form.save()
            auth_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, auth_user)   # Log in authenticate user
            return render(request, 'home.html')
    context = {'form': form}
    return render(request, 'registration.html', context)


def logout_view(request):
    """Log out users"""
    logout(request)
    return render(request, 'home.html')


def submit_order(request):
    return render(request, 'submit_order.html')


def submit_order_appearance(request):
    return render(request, 'submit_order_appearance.html')


def submit_order_coffin(request):
    return render(request, 'submit_order_coffin.html')


def submit_order_flower(request):
    return render(request, 'submit_order_flower.html')


def submit_order_music(request):
    return render(request, 'submit_order_music.html')


def submit_order_summary(request):
    return render(request, 'submit_order_summary.html')


def your_order(request):
    return render(request, 'your_order.html')


def user_account(request):
    return render(request, 'user_account.html')


def edit_user(request):
    return render(request, 'edit_user.html')


def change_password(request):
    return render(request, 'change_password.html')


def delete_user(request):
    return render(request, 'delete_user.html')
