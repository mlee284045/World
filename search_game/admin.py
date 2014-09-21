from django.contrib import admin
from search_game.models import City
# Register your models here.


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass