from django.contrib.auth.models import User
from django.db import models

from main.utils import REVIEW_CHOICES


class Reviews(models.Model):
    """Reviews about the company"""

    description = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=REVIEW_CHOICES, default=1)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
