from django import forms
from django.contrib.auth import forms as form
from .models import Died, Coffin, Flowers, Music, Order, User


class UserCreationForm(form.UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class DiedForm(forms.ModelForm):
    class Meta:
        model = Died
        fields = ['surname', 'name', 'gender', 'date_birthday', 'date_died', 'transcription', 'outfit', 'makeup']
        labels = {'surname': '', 'name': '', 'gender': '', 'date_birthday': '', 'date_died': '', 'transcription': '', \
                  'outfit': '', 'makeup': ''}


class CoffinForm(forms.ModelForm):
    class Meta:
        model = Coffin
        fields = ['description', 'size', 'wood']
        labels = {'description': '', 'size': '', 'wood': ''}


class FlowerForm(forms.ModelForm):
    class Meta:
        model = Flowers
        fields = ['description', 'size', 'color', 'count']
        labels = {'description': '', 'size': '', 'color': '', 'count': '', }


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['msc_type', 'songs']
        labels = {'msc_type': '', 'songs': ''}


# TODO: how to make order form
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
