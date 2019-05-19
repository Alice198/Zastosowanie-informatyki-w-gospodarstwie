from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models

from main.utils import MUSIC_TYPE, MUSIC_LEVEL


class Music(models.Model):
    """Information about music"""

    msc_type = models.CharField(max_length=1, choices=MUSIC_TYPE)
    songs = models.TextField()
    price_M = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        """Returns model as string"""
        return self.songs
