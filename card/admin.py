from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(DebitCard)
class DevitCardAdmin(admin.ModelAdmin):
    list_display = ['id','card_name','card_number','card_cvv','card_balance','card_exp_month','card_exp_year']