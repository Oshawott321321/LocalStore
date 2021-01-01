from django import forms
from django.core import validators
from django.forms import ModelForm
from .models import *
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class CreateUserForm(UserCreationForm):
    password2 = forms.CharField(label = 'Confirm',
                                widget=forms.PasswordInput)
    class Meta:
        model = OWNUSER
        fields = ['username','first_name','last_name','email','mobile_no','state','city','area']
        labels = {'email':'Email','password2':'Confirm'}

class ProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = OWNUSER
        # fields = '__all__'
        fields = ['username','first_name','last_name','email','mobile_no','last_login']

class AdminProfileForm(UserChangeForm):
    class Meta:
        model = OWNUSER
        fields = '__all__'
        exclude = ['password']