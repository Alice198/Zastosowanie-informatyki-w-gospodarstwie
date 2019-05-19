from django.contrib.auth.models import User
from django.db import models

# from main.models.order import Order
from main.utils import FLOWERS_SIZE, FLOWERS_COLOR


class Flowers(models.Model):
    """Information about flowers"""

    size = models.CharField(max_length=1, choices=FLOWERS_SIZE)
    color = models.CharField(max_length=2, choices=FLOWERS_COLOR)
    count = models.IntegerField()
    description = models.CharField(max_length=200, null=True, blank=True)
    price_F = models.DecimalField(decimal_places=2, max_digits=7, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        """Returns model as string"""
        return self.description
