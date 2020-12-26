from django.db import models
from appuser.models import OWNUSER,Area
from django.core import validators
# Create your models here.




class Week(models.Model):
    day = models.CharField(max_length=15)

    def __str__(self):
        return self.day


class Shop(models.Model):
    shop_owner = models.ForeignKey(OWNUSER, on_delete=models.CASCADE)
    shop_address_area = models.ForeignKey(Area, on_delete=models.CASCADE)
    shop_name =models.CharField( max_length=100 , null = True)
    shop_address =models.CharField( max_length= 500 ,null=True )
    shop_image = models.ImageField( null = True ,blank = True,upload_to='shops')#,height_field=hw, width_field=hw)
    shop_contact = models.CharField(max_length=10,null=True)
    shop_open_time = models.TimeField(auto_now=True, auto_now_add=False)
    shop_close_time = models.TimeField(auto_now=True, auto_now_add=False)
    shop_days = models.ManyToManyField(Week)


    def __str__(self):
        return self.shop_name


class Product(models.Model):
    pro_shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    pro_name = models.CharField(max_length=100,blank = False)
    pro_price = models.FloatField(blank=False)
    pro_image = models.ImageField( null = True ,blank = True,upload_to='product')#,height_field=hw, width_field=hw) 
    pro_des = models.CharField(blank=True, max_length=1000)
    pro_quantity = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    cart_user = models.ForeignKey(OWNUSER,on_delete=models.CASCADE,null=True)#unique =True

    def __str__(self):
        return str(self.id) + "-" + self.cart_user.username
    

class Cart_Product(models.Model):
    cart_id = models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
    cart_product_id = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    cart_product_quantity = models.PositiveSmallIntegerField()

    
class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,null=True)
    order_amount = models.PositiveIntegerField()
    order_address = models.CharField(max_length=300,null=True)

class ConfirmedOrder(models.Model):
    user =  models.CharField( max_length=100)
    total = models.IntegerField()
    address = models.CharField( max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "O-id: " + str(self.id) + " | User: " + self.user


class Ordered_Product(models.Model):
    order = models.ForeignKey(ConfirmedOrder, on_delete=models.CASCADE)
    shop = models.CharField( max_length=100)
    name = models.CharField(max_length=100,blank = False)
    price = models.FloatField(null=True)
    quantity = models.PositiveIntegerField(default = 0)
    