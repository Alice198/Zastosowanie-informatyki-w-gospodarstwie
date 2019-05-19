from django.contrib.auth.models import User
from django.db import models

from main.models.coffin import Coffin
from main.models.died import Died
from main.models.flowers import Flowers
from main.models.music import Music


class Order(models.Model):
    """Full order information"""

    is_finished = models.BooleanField(default=False)
    order_date = models.DateField(auto_now_add=True)
    costs = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    died = models.OneToOneField(Died, on_delete=models.CASCADE, null=True, blank=True)
    coffin = models.OneToOneField(Coffin, on_delete=models.CASCADE, null=True, blank=True)
    music = models.ForeignKey(Music, on_delete=models.CASCADE, null=True, blank=True)
    flowers = models.ForeignKey(Flowers, on_delete=models.CASCADE, null=True, blank=True)

    # def __str__(self):
    #     """Returns model as string"""
    #     return str(self.user.id)
