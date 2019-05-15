from django.contrib.auth.models import User
from django.db import models

# from main.models.order import Order
from main.utils import MUSIC_TYPE


class Music(models.Model):
    """Information about music"""

    msc_type = models.CharField(max_length=1, choices=MUSIC_TYPE)
    songs = models.TextField()
    # telephone_num = models.DecimalField(max_digits=9, decimal_places=0)
    # price = models.DecimalField(decimal_places=2, max_digits=4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        """Returns model as string"""
        return self.songs
