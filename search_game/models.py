from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=2)
    latitude = models.DecimalField(max_digits=7, decimal_places=4)
    longitude = models.DecimalField(max_digits=7, decimal_places=4)

    def __unicode__(self):
        return self.name

    def arrive(self):
        self.current = True
        self.visited = True

    def leave(self):
        self.current = False


class Balance(models.Model):
    hidden = models.IntegerField(default=1)
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

    def arrive(self, city_id):
        self.current_city = city_id
        # self.visited_cities = self.visited_cities + ',{}'.format(city_id)

    def minus_money(self, monies):
        self.money -= monies
        return self.money

    def update_time(self, time):
        self.start = time
        return self.start

    def get_time_left_hours(self):
        time_left = self.end - self.start
        seconds = time_left.total_seconds()
        return seconds / 3600

    def get_time_left_days(self):
        return int(self.get_time_left_hours() / 24)
