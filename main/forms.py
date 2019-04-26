from django import forms
from .models import Died, Coffin, Flowers, Music, Order


class DiedForm(forms.ModelForm):
    class Meta:
        model = Died
        fields = ['surname', 'name', 'gender', 'date_birthday', 'date_died', 'transcription']
        labels = {'surname': '', 'name': '', 'gender': '', 'date_birthday': '', 'date_died': '', 'transcription': ''}


class DiedLookForm(forms.ModelForm):
    class Meta:
        model = Died
        fields = ['outfit', 'makeup']
        labels = {'outfit': '', 'makeup': ''}


class CoffinForm(forms.ModelForm):
    class Meta:
        model = Coffin
        fields = ['description', 'size', 'wood']
        labels = {'description': '', 'size': '', 'wood': ''}


class FlowerForm(forms.ModelForm):
    class Meta:
        model = Flowers
        fields = ['description', 'size', 'color', 'count', 'price']
        labels = {'description': '', 'size': '', 'color': '', 'count': '', 'price': ''}


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['msc_type', 'telephone_num', 'price']
        labels = {'msc_type': '', 'telephone_num': '', 'price': ''}


# TODO: how to make order form
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = []
