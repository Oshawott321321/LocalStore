from django import forms
from django.core import validators
from django.forms import ModelForm
from card.models import *
from product.models import Order

class FormCard(forms.ModelForm):
    class Meta:
        model = DebitCard
        # fields ='__all__'
        fields = ["card_number","card_cvv","card_name","card_exp_month","card_exp_year"]

    def clean(self):
        data = self.cleaned_data

        card_number = data.get("card_number") 
        card_cvv = data.get("card_cvv") 
        card_name = data.get("card_name") 
        card_exp_month = data.get("card_exp_month") 
        card_exp_year = data.get("card_exp_year") 

        temp = DebitCard.objects.filter(card_number = card_number)
        if not temp.exists():
            raise forms.ValidationError("This Info is not right")
        qs= temp[0]

        if card_cvv != qs.card_cvv:
            raise forms.ValidationError("CVv Error")
        # if card_number != qs.card_number:
        #     raise forms.ValidationError("nu Error")
        if card_name != qs.card_name:
            raise forms.ValidationError("name Error")
        if card_exp_month != qs.card_exp_month:
            raise forms.ValidationError("month Error")
        if card_exp_year != qs.card_exp_year:
            raise forms.ValidationError("year Error")

        return 
        

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['order_address']