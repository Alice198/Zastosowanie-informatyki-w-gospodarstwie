from django.db import models
from .utils import *


class User(models.Model):

    username = models.TextField()
    password1 = models.TextField()
    name = models.TextField()
    surname = models.TextField()
    telephone_num = models.IntegerField()
    email = models.EmailField()


class Reviews(models.Model):
    """Reviews about the company"""

    description = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=REVIEW_CHOICES, default=1)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class Died(models.Model):

    name = models.TextField()
    surname = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_birthday = models.DateField()
    date_died = models.DateField()
    transcription = models.CharField(max_length=50)
    outfit = models.CharField(max_length=200)
    makeup = models.CharField(max_length=100)


class Coffin(models.Model):

    wood = models.CharField(max_length=1, choices=TYPE_WOOD)
    size = models.CharField(max_length=1, choices=COFFIN_SIZE)
    description = models.CharField(max_length=200)


class Order(models.Model):

    order_date = models.DateField(auto_now_add=True)
    costs = models.DecimalField(decimal_places=2, max_digits=6)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    died = models.OneToOneField(Died, on_delete=models.PROTECT)
    coffin = models.OneToOneField(Coffin, on_delete=models.PROTECT)


class Flowers(models.Model):

    size = models.CharField(max_length=1, choices=FLOWERS_SIZE)
    color = models.CharField(max_length=2, choices=FLOWERS_COLOR)
    count = models.IntegerField()
    description = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)


class Music(models.Model):

    msc_type = models.CharField(max_length=1, choices=MUSIC_TYPE)
    telephone_num = models.DecimalField(max_digits=9, decimal_places=0)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    order = models.OneToOneField(Order, on_delete=models.PROTECT)
