from django.urls import path
from .views import *

urlpatterns = [
    path('',Profile,name='Profile'),
    
    path('register/',register_user,name="Register"),
    path('login/',login_user,name="Login"),
    path('logout/',log_out,name="logout"),

    path('change_pass/',change_pass,name="ChangePassword"),
    path('change_pass1/',change_pass1,name="ChangePassword1"),
    
    path('show_data/<str:id>/',show_data,name="show_data"),
    
    path('create_shop/',create_shop,name="Create_shop"),
    path('delete_shop/<int:pk>/',delete_shop,name="Delete_shop"),
    path('update_shop/<int:pk>/',update_shop,name="Update_shop"),
]