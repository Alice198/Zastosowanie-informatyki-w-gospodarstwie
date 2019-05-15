from django import forms
from django.contrib.auth import forms as form
from django.contrib.auth.models import User

from main.models.coffin import Coffin
from main.models.died import Died
from main.models.flowers import Flowers
from main.models.music import Music
from main.models.order import Order


class UserCreationForm(form.UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class GetPasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password']


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


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
