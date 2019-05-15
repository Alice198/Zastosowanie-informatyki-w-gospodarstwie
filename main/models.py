from django.contrib.auth.models import User
from django.db import models
from .utils import *


# class User(models.Model):
#     """User data"""
#
#     username = models.TextField()
#     password1 = models.TextField()
#     name = models.TextField()
#     surname = models.TextField()
#     telephone_num = models.IntegerField()
#     email = models.EmailField()


class Reviews(models.Model):
    """Reviews about the company"""

    description = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=REVIEW_CHOICES, default=1)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class Died(models.Model):
    """Information about died"""

    name = models.TextField()
    surname = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_birthday = models.DateField()
    date_died = models.DateField()
    transcription = models.CharField(max_length=50)
    outfit = models.CharField(max_length=200)
    makeup = models.CharField(max_length=1, choices=MAKEUP_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        """Returns model as string"""
        return self.surname


class Coffin(models.Model):
    """Information about coffin"""

    wood = models.CharField(max_length=1, choices=TYPE_WOOD)
    size = models.CharField(max_length=1, choices=COFFIN_SIZE)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        """Returns model as string"""
        return self.description


class Flowers(models.Model):
    """Information about flowers"""

    size = models.CharField(max_length=1, choices=FLOWERS_SIZE)
    color = models.CharField(max_length=2, choices=FLOWERS_COLOR)
    count = models.IntegerField()
    description = models.CharField(max_length=200, null=True, blank=True)
    # price = models.DecimalField(decimal_places=2, max_digits=4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        """Returns model as string"""
        return self.description


class Music(models.Model):
    """Information about music"""

    msc_type = models.CharField(max_length=1, choices=MUSIC_TYPE)
    songs = models.TextField()
    # telephone_num = models.DecimalField(max_digits=9, decimal_places=0)
    # price = models.DecimalField(decimal_places=2, max_digits=4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        """Returns model as string"""
        return self.songs


class Order(models.Model):
    """Full order information"""

    is_finished = models.BooleanField(default=False)
    order_date = models.DateField(auto_now_add=True)
    costs = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    died = models.OneToOneField(Died, on_delete=models.CASCADE, null=True, blank=True)
    coffin = models.OneToOneField(Coffin, on_delete=models.CASCADE, null=True, blank=True)
    music = models.ForeignKey(Music, on_delete=models.CASCADE, null=True, blank=True)
    flowers = models.ForeignKey(Flowers, on_delete=models.CASCADE, null=True, blank=True)

    # def __str__(self):
    #     """Returns model as string"""
    #     return str(self.user.id)
