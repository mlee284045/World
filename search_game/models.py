from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=2)
    latitude = models.DecimalField(max_digits=7, decimal_places=4)
    longitude = models.DecimalField(max_digits=7, decimal_places=4)
    users = models.ManyToManyField(User, through='Location', blank=True)


class Location(models.Model):
    current = models.BooleanField(default=True)
    user = models.ForeignKey(User)
    city = models.ForeignKey(City)


class Balance(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    money = models.DecimalField(max_digits=7, decimal_places=2)
    user = models.OneToOneField(User, related_name='balance')