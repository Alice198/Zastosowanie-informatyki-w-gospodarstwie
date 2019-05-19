from django.contrib.auth.models import User
from django.db import models

from main.utils import TYPE_WOOD, COFFIN_SIZE


class Coffin(models.Model):
    """Information about coffin"""

    wood = models.CharField(max_length=1, choices=TYPE_WOOD)
    size = models.CharField(max_length=1, choices=COFFIN_SIZE)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    price_C = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)

    def __str__(self):
        """Returns model as string"""
        return self.description
