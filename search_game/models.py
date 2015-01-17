from django.contrib.auth.models import User
from django.db import models
from datetime import timedelta, datetime
from random import randint

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=2)
    latitude = models.DecimalField(max_digits=7, decimal_places=4)
    longitude = models.DecimalField(max_digits=7, decimal_places=4)

    def __unicode__(self):
        return self.name


class Balance(models.Model):
    hidden = models.IntegerField(default=1)
    restarts = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    current_city = models.IntegerField(default=2)
    visited_cities = models.CommaSeparatedIntegerField(blank=True, null=True, max_length=200)

    start = models.DateTimeField(blank=True)
    end = models.DateTimeField(null=True, blank=True)
    money = models.DecimalField(max_digits=7, decimal_places=2, default=5000.00)
    found = models.BooleanField(default=False)
    user = models.OneToOneField(User, related_name='balance')

    def add_money(self, monies):
        self.money += monies
        return self.money

    def arrive(self, City_id):
        self.current_city = city_id
        # self.visited_cities = self.visited_cities + ',{}'.format(city_id)

    def minus_money(self, monies):
        self.money -= monies
        return self.money

    def reset(self):
        if self.found:
            self.wins += 1
        self.restarts += 1
        self.start = datetime.now()
        self.end = self.start + timedelta(days=14)
        self.money = 5000.00
        self.visited_cities = "2,"
        self.hidden = randint(1, 23)
        self.save()


    def update_time(self, time):
        self.start = time
        return self.start

    def get_time_left_hours(self):
        time_left = self.end - self.start
        seconds = time_left.total_seconds()
        return seconds / 3600

    def get_time_left_days(self):
        return int(self.get_time_left_hours() / 24)
