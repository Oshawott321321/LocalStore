from django.urls import path
from .views import *

urlpatterns = [
    path('myshop/<int:pk>/',myshop,name='Myshop'),

    path('show_cart/',show_cart,name='Show_Cart'),
    path('add_cart/<int:pk>',add_to_cart,name='add_to_cart'),

    path('create/<int:pk>/',create_product,name='Create-Product'),
    path('update_pro/<int:pk>',update_product,name='Update_product'),
    path('delete_pro/<int:pk>',delete_product,name='Delete_product'),
    path('productinfo/<int:pk>/',product_info,name='Productinfo'),
    
    

    path('increase/<int:cpid>',increase,name='Increase'),
    path('decrease/<int:cpid>',decrease,name='Decrease'),
    path('remove_cp/<int:cpid>',remove_cp,name='Remove_cp'),#cp = cart_product id


]