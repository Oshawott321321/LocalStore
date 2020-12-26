from django.urls import path
from .views import *

urlpatterns = [
    path('detail/<int:o_id>/',enter_detail,name='enter_detail'),
    path('payment/<str:c_id>/',payment,name='Payment'),
    path('order_placed/',order_placed,name='Order_Placed'),
]