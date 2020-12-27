from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    list_display = ['id','day']

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id','shop_owner','shop_name','shop_image','shop_open_time','shop_close_time']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','pro_shop','pro_name','pro_price','pro_image','pro_des']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','cart_user']


@admin.register(Cart_Product)
class Cart_ProductAdmin(admin.ModelAdmin):
    list_display = ['id','cart_id','cart_product_id','cart_product_quantity']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','cart','order_amount','order_address']


@admin.register(ConfirmedOrder)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','user','total','address','date_time']


@admin.register(Ordered_Product)
class Order_ProductAdmin(admin.ModelAdmin):
    list_display = ['id','order','shop','name','price','quantity']