from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(OWNUSER)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['id','state_name']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id','city_name','city_state']


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['id','area_name','area_city']