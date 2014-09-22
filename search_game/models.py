from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=2)
    latitude = models.DecimalField(max_digits=7, decimal_places=4)
    longitude = models.DecimalField(max_digits=7, decimal_places=4)
    users = models.ManyToManyField(User, through='Location', blank=True)

    def __unicode__(self):
        return self.name


class Location(models.Model):
    current = models.BooleanField(default=True)
    user = models.ForeignKey(User, related_name='location')
    city = models.ForeignKey(City, related_name='location')


class Balance(models.Model):
    start = models.DateTimeField(blank=True)
    end = models.DateTimeField(null=True, blank=True)
    money = models.DecimalField(max_digits=7, decimal_places=2, default=5000.00)
    found = models.BooleanField(default=False)
    user = models.OneToOneField(User, related_name='balance')

    def add_money(self, monies):
        self.money += monies
        return self.money

    def minus_money(self, monies):
        self.money -= monies
        return self.money

    def update_time(self, time):
        self.start = time
        return self.start

    def get_time_left_hours(self):
        time_left = self.end - self.start
        seconds = time_left.total_seconds()
        return seconds/3600

    def get_time_left_days(self):
        return self.get_time_left_hours()/24
