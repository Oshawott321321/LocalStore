from django.urls import path
from .views import *

urlpatterns = [
    path("create_card/", create_debit_card, name="Create-Card"),
]