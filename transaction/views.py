from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from card.models import DebitCard
from product.models import Cart,Cart_Product,Order,ConfirmedOrder,Ordered_Product

import datetime

# Create your views here.

def enter_detail(request,o_id):
    if not request.user.is_authenticated:
        redirect('Login')
    
    form = FormCard()
    
    if request.method == 'POST':
        form = FormCard(request.POST)
        if form.is_valid():
            card_no = form.cleaned_data.get('card_number')
            card_obj = DebitCard.objects.get(card_number = card_no)
            card_bal = card_obj.card_balance
            order_obj = Order.objects.get(id = o_id)
            if card_bal < order_obj.order_amount:
                messages.error(request,"Your account don't have Enough money to order")
                return redirect('enter_detail',o_id = o_id)

            # Debit Logic
            new_bal = card_bal - order_obj.order_amount
            DebitCard.objects.filter(card_number = card_no).update(card_balance = new_bal )
            
            # Order Placed

        # This Block Will create Final Orders Which have no connection to our dynamic datasets
            # Creating ConfirmedOrder Data
            coorder = ConfirmedOrder.objects.create(user = request.user.username , total = order_obj.order_amount ,address = order_obj.order_address)

            # Creating Ordered_Products Data

            cpqs = Cart_Product.objects.filter(cart_id = order_obj.cart.id)
            for i in cpqs:
                Ordered_Product.objects.create( order = coorder , shop = i.cart_product_id.pro_shop.shop_name ,name = i.cart_product_id.pro_name , price = i.cart_product_id.pro_price ,quantity = i.cart_product_quantity )

            # Deleting  Cart from Database , so it will delete Its Cart_Product and Order object


            order_obj.cart.delete()
            


        # End block

            return redirect('Order_Placed')
        else:
            #debitcard is not valid 
            messages.error(request,"Card Details Are Wrong")
            return redirect('enter_detail',o_id = o_id)
    global_card = DebitCard.objects.get(id=1)
    context={ 'form':form ,"global_card":global_card ,"o_id":o_id}
    return render(request,'transaction/enter_data.html',context)




def payment(request ,c_id ):
    if not request.user.is_authenticated:
        return redirect('Home_Page')
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)  # here order obj is created
            cart_obj = Cart.objects.filter(id=c_id)
            order_obj = Order.objects.filter(cart = cart_obj[0]) # for checking that is order exist

            if order_obj.exists():

                # Order Already Exist so address is updating  
                order_obj.update(order_address = form.cleaned_data.get('order_address'))

                print("order already ecisit")
                return redirect('enter_detail',o_id = order_obj[0].id)
                # return render(request,'transaction/payment.html',context={})

            
            cart_products = Cart_Product.objects.filter(cart_id = c_id)
            total = 0
            for product in cart_products:
                total+= product.cart_product_id.pro_price * product.cart_product_quantity
            form_obj.cart = cart_obj[0]
            # form_obj.order_date = datetime.datetime.now()
            form_obj.order_amount = total
            # form_obj.order_user = request.user
            form_obj.save()
            order_obj = Order.objects.filter(cart = cart_obj[0])
            return redirect('enter_detail',o_id=order_obj[0].id)
    # db_balance = (DebitCard.objects.get(card_number=pk)).card_balance
    context={ 'form':form ,'cart_obj': c_id  }
    return render(request,'transaction/payment.html',context)
    


def order_placed(request):
    context={}
    return render(request,"transaction/order_placed_message.html",context)

