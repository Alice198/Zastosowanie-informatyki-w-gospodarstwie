from django.contrib.auth.models import User
from django.db import models

# from main.models.order import Order
from main.utils import GENDER_CHOICES, MAKEUP_CHOICES


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
    # order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        """Returns model as string"""
        return self.surname
