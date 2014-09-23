from django.contrib import admin
from search_game.models import City, Balance
# Register your models here.


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    pass

# @admin.register(Location)
# class LocationAdmin(admin.ModelAdmin):
#     pass