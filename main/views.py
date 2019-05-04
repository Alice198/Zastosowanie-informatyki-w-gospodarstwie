# Create your views here.
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Order, Died, Coffin, Flowers, Music
from .forms import DiedForm, CoffinForm, FlowerForm, UserCreationForm


def home(request):
    return render(request, 'home.html')


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
    print(form.errors)
    return render(request, 'registration.html', context)


def logout_view(request):
    """Log out users"""
    logout(request)
    return render(request, 'home.html')


@login_required
def submit_order(request):
    """Add information about died"""
    if request.method != 'POST':
        form = DiedForm()
    else:
        form = DiedForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = User.objects.get(id=request.user.id)
            new_form.save()
            return render(request, 'submit_order_appearance.html')

    context = {'formErrors': form.errors}
    return render(request, 'submit_order.html', context)


@login_required
def submit_order_appearance(request):
    # """Add information about died appearance"""
    # if request.method != 'POST':
    #     form = DiedLookForm()
    # else:
    #     form = DiedLookForm(request.POST)
    #     if form.is_valid():
    #         new_form = form.save(commit=False)
    #         new_form.owner = request.user
    #         new_form.save()
    #         return render(request, 'home.html')
    # context = {'form': form}
    return render(request, 'submit_order_appearance.html',)


@login_required
def submit_order_coffin(request):
    """Add information about coffin"""
    if request.method != 'POST':
        form = CoffinForm()
    else:
        form = CoffinForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = User.objects.get(id=request.user.id)
            new_form.save()
            return render(request, 'submit_order_flower.html')
    context = {'formErrors': form.errors}
    return render(request, 'submit_order_coffin.html', context)


# TODO: naprawic formularz jw
@login_required
def submit_order_flower(request):
    """Add information about flowers"""
    if request.method != 'POST':
        form = FlowerForm()
    else:
        form = FlowerForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = User.objects.get(id=request.user.id)
            new_form.save()
            return render(request, 'submit_order_music.html')
    context = {'formErrors': form.errors}
    return render(request, 'submit_order_flower.html', context)

# TODO: naprawic formularz jw
@login_required
def submit_order_music(request):
    """Add information about music"""
    if request.method != 'POST':
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
    try:
        died_query = Died.objects.get(user=request.user)
    except:
        died_query = None
    try:
        coffin_query = Coffin.objects.get(user=request.user)
    except:
        coffin_query = None
    try:
        flowers_query = Flowers.objects.get(user=request.user)
    except:
        flowers_query = None
    try:
        music_query = Music.objects.get(user=request.user)
    except:
        music_query = None

    if request.method == 'POST':
        # TODO: logika do liczenia ceny całkowitej (if coffin_qery.wood == oak: wood_price = 200
        # total_price = coffin_query.price + music_query.price
        pass
        # TODO: tworzenie obiektu order, to jest akcja klikniecia przycusku Potwierdź w podsumowaniu zamówienia
        # Obiekt order ma zawierać wszystkie wyżej pola
        # Order.objects.create(
        #     died=died_query,
        #     coffin=coffin_query,
        #     music=music_query,
        #     flowers=flowers_query,
        #     user=User.objects.get(id=request.user.id),
        #     # costs=total_price
        # )
    context = {
        'died': died_query,
        'coffin': coffin_query,
        'flowers': flowers_query,
        'music': music_query,
    }
    return render(request, 'submit_order_summary.html', context)


@login_required
def your_order(request):
#     order = Order.objects.filter(owner=request.user).order_by('order_date')
#     context = {'order': order}
    return render(request, 'your_order.html', )


def user_account(request):
    return render(request, 'user_account.html')


def edit_user(request):
    return render(request, 'edit_user.html')


def change_password(request):
    if request.method != 'POST':
        form = PasswordChangeForm(request.user)   # Empty form
    else:
        form = PasswordChangeForm(request.user, data=request.POST)  # Fill fo
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Twoje haslo zostalo pomyslnie zmienione')
            return redirect('Change password')
        else:
            messages.error(request, 'Prosze poprawic dane')
    context = {'form': form}
    return render(request, 'change_password.html', context)


def delete_user(request):
    return render(request, 'delete_user.html')


def opinion(request):
    return render(request, 'opinion.html')
