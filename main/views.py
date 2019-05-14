from django.contrib import messages
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Order, Died, Coffin, Flowers, Music
from .forms import DiedForm, CoffinForm, FlowerForm, UserCreationForm, MusicForm


def check_and_save_form(request, form, template):
    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.user = User.objects.get(id=request.user.id)
        new_form.save()
        # return render(request, template)
        return new_form


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


def get_order(request):
    try:
        open_order = Order.objects.filter(user=request.user, is_finished=False)[0]
    except:
        open_order = None
    if not open_order:
        open_order = Order.objects.create(user=User.objects.get(id=request.user.id))

    return open_order


@login_required
def submit_order(request):
    """Add information about died"""
    current_order = get_order(request)
    try:
        died_query = Died.objects.get(id=current_order.died.id)
    except:
        died_query = None

    if died_query:
        if request.method != 'POST':
            date_b = died_query.date_birthday.strftime("%Y-%m-%d")
            date_d = died_query.date_died.strftime("%Y-%m-%d")
            context = {'died': died_query, 'birthday': date_b, 'death': date_d}
            return render(request, 'submit_order.html', context)
        else:
            died_query.delete()
            form = DiedForm(request.POST)
            died = check_and_save_form(request, form, 'submit_order_coffin.html')
            current_order.died = died
            current_order.save()
            # return render(request, 'submit_order_coffin.html')
        new_query = Died.objects.get(user=request.user, id=current_order.died.id)
        date_b = died_query.date_birthday.strftime("%Y-%m-%d")
        date_d = died_query.date_died.strftime("%Y-%m-%d")
        context = {'formErrors': form.errors, 'died': new_query, 'birthday': date_b, 'death': date_d}
        return render(request, 'submit_order.html', context)
    else:
        if request.method != 'POST':
            form = DiedForm()
        else:
            form = DiedForm(request.POST)
            died = check_and_save_form(request, form, 'submit_order_coffin.html')
            current_order.died = died
            current_order.save()
            died_query = Died.objects.get(id=current_order.died.id)
        context = {'formErrors': form.errors, 'died': died_query}
        return render(request, 'submit_order.html', context)


@login_required
def submit_order_coffin(request):
    """Add information about coffin"""
    current_order = get_order(request)
    try:
        coffin_query = Coffin.objects.get(id=current_order.coffin.id)
    except:
        coffin_query = None

    if coffin_query:
        if request.method != 'POST':
            context = {'coffin': coffin_query}
            return render(request, 'submit_order_coffin.html', context)
        else:
            coffin_query.delete()
            form = CoffinForm(request.POST)
            coffin = check_and_save_form(request, form, 'submit_order_flower.html')
            current_order.coffin = coffin
            current_order.save()
        new_query = Coffin.objects.get(user=request.user, id=current_order.coffin.id)
        context = {'formErrors': form.errors, 'coffin': new_query}
        return render(request, 'submit_order_coffin.html', context)
    else:
        if request.method != 'POST':
            form = CoffinForm()
        else:
            form = CoffinForm(request.POST)
            coffin = check_and_save_form(request, form, 'submit_order_flower.html')
            current_order.coffin = coffin
            current_order.save()
            coffin_query = Coffin.objects.get(id=current_order.coffin.id)
        context = {'formErrors': form.errors, 'coffin': coffin_query}
        return render(request, 'submit_order_coffin.html', context)


@login_required
def submit_order_flower(request):
    """Add information about flowers"""
    current_order = get_order(request)
    try:
        flowers_query = Flowers.objects.get(id=current_order.flowers.id)
    except:
        flowers_query = None

    if flowers_query:
        if request.method != 'POST':
            context = {'flower': flowers_query}
            return render(request, 'submit_order_flower.html', context)
        else:
            flowers_query.delete()
            form = FlowerForm(request.POST)
            flowers = check_and_save_form(request, form, 'submit_order_music.html')
            current_order.flowers = flowers
            current_order.save()
        new_query = Flowers.objects.get(user=request.user, id=current_order.flowers.id)
        context = {'formErrors': form.errors, 'flower': new_query}
        return render(request, 'submit_order_flower.html', context)
    else:
        if request.method != 'POST':
            form = FlowerForm()
        else:
            form = FlowerForm(request.POST)
            flowers = check_and_save_form(request, form, 'submit_order_music.html')
            current_order.flowers = flowers
            current_order.save()
            flowers_query = Flowers.objects.get(id=current_order.flowers.id)
        context = {'formErrors': form.errors, 'flowers': flowers_query}
        return render(request, 'submit_order_flower.html', context)


@login_required
def submit_order_music(request):
    """Add information about music"""
    # exist_musics = Music.objects.filter(user=request.user).values('id')
    # try:
    #     orders = Order.objects.filter(user=request.user, music__in=exist_musics)
    # except:
    #     orders = None
    current_order = get_order(request)
    try:
        music_query = Music.objects.get(id=current_order.music.id)
    except:
        music_query = None

    if music_query:
        if request.method != 'POST':
            context = {'music': music_query}
            return render(request, 'submit_order_music.html', context)
        else:
            music_query.delete()
            form = MusicForm(request.POST)
            music = check_and_save_form(request, form, 'submit_order_summary.html')
            current_order.music = music
            current_order.save()
        new_query = Music.objects.get(user=request.user, id=current_order.music.id)
        context = {'formErrors': form.errors, 'music': new_query}
        return render(request, 'submit_order_music.html', context)
    else:
        if request.method != 'POST':
            form = MusicForm()
        else:
            form = MusicForm(request.POST)
            music = check_and_save_form(request, form, 'submit_order_summary.html')
            current_order.music = music
            current_order.save()
            music_query = Music.objects.get(id=current_order.music.id)
        context = {'formErrors': form.errors, 'music': music_query}
        return render(request, 'submit_order_music.html', context)


@login_required
def submit_order_summary(request):
    # try:
    #     died_query = Died.objects.get(user=request.user)
    # except:
    #     died_query = None
    # try:
    #     coffin_query = Coffin.objects.get(user=request.user)
    # except:
    #     coffin_query = None
    # try:
    #     flowers_query = Flowers.objects.get(user=request.user)
    # except:
    #     flowers_query = None
    # try:
    #     music_query = Music.objects.get(user=request.user)
    # except:
    #     music_query = None

    current_order = get_order(request)

    try:
        died_query = Died.objects.get(id=current_order.died.id)
    except:
        died_query = None
    try:
        coffin_query = Coffin.objects.get(id=current_order.coffin.id)
    except:
        coffin_query = None
    try:
        flowers_query = Flowers.objects.get(id=current_order.flowers.id)
    except:
        flowers_query = None
    try:
        music_query = Music.objects.get(id=current_order.music.id)
    except:
        music_query = None
    # TODO: logika do liczenia ceny całkowitej (if coffin_qery.wood == oak: wood_price = 200
    total_price = 2000.05    # coffin_query.price + music_query.price

    if request.method == 'POST':
        current_order.is_finished = True
        current_order.costs = total_price
        current_order.save()

        # Order.objects.get_or_create(
        #     died=died_query,
        #     coffin=coffin_query,
        #     music=music_query,
        #     flowers=flowers_query,
        #     user=User.objects.get(id=request.user.id),
        #     costs=total_price,
        #     is_finished=True
        # )

        context = {
            'died': died_query,
            'coffin': coffin_query,
            'flowers': flowers_query,
            'music': music_query,
            'costs': total_price
        }
        return render(request, 'your_order.html', context)
    context = {
        'died': died_query,
        'coffin': coffin_query,
        'flowers': flowers_query,
        'music': music_query,
        'costs': total_price
    }
    return render(request, 'submit_order_summary.html', context)


@login_required
def your_order(request):
    order_query = Order.objects.filter(user=request.user, is_finished=True).order_by('order_date')
    print(order_query)

    for order in order_query:
        print(order.costs)

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
    try:
        total_costs = order_query.costs
    except:
        total_costs = None

    context = {
        'died': died_query,
        'coffin': coffin_query,
        'flowers': flowers_query,
        'music': music_query,
        'costs': total_costs,
        'order': order_query,
    }
    return render(request, 'your_order.html', context={'orders': order_query})


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


def edit_your_order(request):
    return render(request, 'edit_your_order.html')


def submit_order_appearance():
    pass
