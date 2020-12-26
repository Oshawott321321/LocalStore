from django.urls import path
from .views import *

urlpatterns = [
    # path('create/',create_product,name='Create-Product'),
    path('add_cart/<int:pk>',add_to_cart,name='add_to_cart'),
    path('show_cart/',show_cart,name='Show_Cart'),
    path('increase/<int:cpid>',increase,name='Increase'),
    path('decrease/<int:cpid>',decrease,name='Decrease'),
    path('remove_cp/<int:cpid>',remove_cp,name='Remove_cp'),
    path('productinfo/<int:pk>/',product_info,name='Productinfo'),
]