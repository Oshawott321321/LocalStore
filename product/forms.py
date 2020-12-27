from django import forms

from .models import *

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product 
        fields = '__all__'
        exclude = ['pro_shop']

class ShopForm(forms.ModelForm):

    class Meta:
        model = Shop
        fields = '__all__'
        exclude = ['shop_owner']