from django.db import models


# Create your models here.


class User(models.Model):
    GENDER_CHOICES = (
        ('F', _('Female')),
        ('M', _('Man')),
    )

    login = models.TextField()
    password = models.TextField()
    name = models.TextField()
    surname = models.TextField()
    telephone_num = models.IntegerField(max_length=9)
    email = models.EmailField()


class Reviews(models.Model):
    """Reviews about the company"""
    REVIEW_CHOICES = (
        (1, _('One star')),
        (2, _('Two stars')),
        (3, _('Three stars')),
        (4, _('Four stars')),
        (5, _('Five stars')),
    )

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
    TYPE_WOOD = (
        ('O', _('Oak')),
        ('B', _('Beech')),
        ('P', _('Pine'))
    )
    COFFIN_SIZE = (
        ('A', _('Adult')),
        ('C', _('Chd')),
    )

    wood = models.CharField(max_length=1, choices=TYPE_WOOD)
    size = models.CharField(max_length=1, choices=COFFIN_SIZE)
    description = models.CharField(max_length=200)


class Order(models.Model):
    order_date = models.DateField(auto_now_add=True)
    costs = models.DecimalField(decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    died = models.OneToOneField(Died, on_delete=models.PROTECT)
    coffin = models.OneToOneField(Coffin, on_delete=models.PROTECT)


class Flowers(models.Model):
    FLOWERS_COLOR = (
        ('Wh', _('White flowers')),
        ('Bl', _('Blue flowers')),
        ('Pi', _('Pink flowers')),
        ('Ot', _('Other color flowers')),
    )
    FLOWERS_SIZE = (
        ('S', _('Small')),
        ('M', _('Medium')),
        ('B', _('Big')),
    )

    size = models.CharField(max_length=1, choices=FLOWERS_SIZE)
    color = models.CharField(max_length=2, choices=FLOWERS_COLOR)
    count = models.IntegerField()
    description = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)


class Music(models.Model):
    MUSIC_TYPE = (
        ('T', _('Trumpet')),
        ('O', _('Organ')),
    )

    msc_type = models.CharField(max_length=1, choices=MUSIC_TYPE)
    telephone_num = models.IntegerField(max_length=9)
    price = models.DecimalField(decimal_places=2)
    order = models.OneToOneField(Order, on_delete=models.PROTECT)
