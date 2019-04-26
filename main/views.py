# Create your views here.
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Order
from .forms import DiedForm, DiedLookForm, CoffinForm, FlowerForm


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


@login_required
def submit_order(request):
    """Add information about died"""
    if request.method != 'POST:':
        form = DiedForm()
    else:
        form = DiedForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.owner = request.user
            new_form.save()
            return render(request, 'home.html')
    context = {'form': form}
    return render(request, 'submit_order.html', context)


@login_required
def submit_order_appearance(request):
    """Add information about died appearance"""
    if request.method != 'POST:':
        form = DiedLookForm()
    else:
        form = DiedLookForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.owner = request.user
            new_form.save()
            return render(request, 'home.html')
    context = {'form': form}
    return render(request, 'submit_order_appearance.html', context)


@login_required
def submit_order_coffin(request):
    """Add information about coffin"""
    if request.method != 'POST:':
        form = CoffinForm()
    else:
        form = CoffinForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.owner = request.user
            new_form.save()
            return render(request, 'home.html')
    context = {'form': form}
    return render(request, 'submit_order_coffin.html', context)


@login_required
def submit_order_flower(request):
    """Add information about flowers"""
    if request.method != 'POST:':
        form = FlowerForm()
    else:
        form = FlowerForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.owner = request.user
            new_form.save()
            return render(request, 'home.html')
    context = {'form': form}
    return render(request, 'submit_order_flower.html', context)


@login_required
def submit_order_music(request):
    """Add information about music"""
    if request.method != 'POST:':
        form = FlowerForm()
    else:
        form = FlowerForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.owner = request.user
            new_form.save()
            return render(request, 'home.html')
    context = {'form': form}
    return render(request, 'submit_order_music.html', context)


@login_required
def submit_order_summary(request):
    return render(request, 'submit_order_summary.html')


@login_required
def your_order(request):
    order = Order.objects.filter(owner=request.user).order_by('order_date')
    context = {'order': order}
    return render(request, 'your_order.html', context)


def user_account(request):
    return render(request, 'user_account.html')


def edit_user(request):
    return render(request, 'edit_user.html')


def change_password(request):
    return render(request, 'change_password.html')


def delete_user(request):
    return render(request, 'delete_user.html')
