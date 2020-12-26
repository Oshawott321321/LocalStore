from django import forms
from django.core import validators
from django.forms import ModelForm
from .models import *

class CardForm(forms.ModelForm):
    class Meta:
        model = DebitCard
        fields = "__all__"