from django.shortcuts import render
from django.contrib import messages
from .forms import *


# Create your views here.


def create_debit_card(request):
    form = CardForm()
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Debit Card Created SUccessfully')
    context = { 'form':form  }
    return render(request,'card/create_card.html',context)