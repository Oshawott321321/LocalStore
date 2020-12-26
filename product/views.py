from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import Http404
from .forms import *
from .models import *

# Create your views here.


def home_page(request):
    context = {}
    context['product_data'] = get_product_data(request)
    return render(request,'product/home_page.html',context)

def get_product_data(request):
    product_data = Product.objects.all()
    return product_data

# def create_product(request):
#     form = ProductForm(request.POST or None , request.FILES or None)
#     if request.method == 'POST':
#         form = ProductForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Product Created')
#         else:
#             messages.success(request,'Form Error')
#     context = { 'form':form ,'user':request.user }
#     return render(request,'product/createproduct.html',context)

def about_developers(request):
    return render(request,'product/developers.html')
            

def product_info(request,pk):
    data = Product.objects.filter(id = pk)
    if not data.exists():
        raise Http404("Invalid URL.THis Product Doesn't Exist")
    context= { 'data' : data[0] }
    return render(request,'product/productinfo.html',context)


def add_to_cart(request,pk):
    if not request.user.is_authenticated:
        messages.info(request,'Please Login First')
        return redirect('Login')

    creating_cart_object(request,pk)
    return redirect('Home_Page')

def creating_cart_object(request,pk):
    temp = Cart.objects.filter(cart_user = request.user) 
    print(temp)
    if not temp:
        # New Cart Object
        cart = Cart(cart_user = request.user)
        cart.save()
        # print("cart created")
        cart_product = Cart_Product(cart_id = cart , cart_product_id = Product.objects.get(id = pk ),cart_product_quantity=1)
        cart_product.save()
    else:
        # Cart EXist so products will be added to exsting cart
        # print("User Exist")
        qs = Cart_Product.objects.filter(cart_id = temp[0],cart_product_id = Product.objects.get(id=pk))
        if qs.exists():
            # print("product exists")
            return
        print("QS : ",qs)
        cart_product = Cart_Product(cart_id = temp[0],cart_product_id = Product.objects.get(id = pk ),cart_product_quantity=1)
        cart_product.save()
    return

def show_cart(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    c_id = Cart.objects.filter(cart_user = request.user)
    if not c_id.exists():
        print("nt extstsir")
        context={ 'cart_id' : None,
              'cart_products': None,
              'USER':request.user,
              'total':0 }
        return render(request,'product/cart.html',context)
    cart_products = Cart_Product.objects.filter(cart_id = c_id[0])
    if not cart_products.exists():
        context = {
                    'cart_id' : None,
                    'cart_products': None,
                    'USER':request.user,
                    'total':0 }
        return render(request,'product/cart.html',context)
    total = 0
    for product in cart_products:
        total+= product.cart_product_id.pro_price * product.cart_product_quantity

    context={ 'cart_id' : c_id[0],
              'cart_products': cart_products,
              'USER':request.user,
              'total':total }
    print(context)
    return render(request,'product/cart.html',context)

def increase(request,cpid):
    if request.user.is_authenticated:
        cpobj = Cart_Product.objects.get(id = cpid)
        cpobj.cart_product_quantity +=1
        cpobj.save()
        return redirect('Show_Cart')
    else:
        return redirect('Home_page')

def decrease(request,cpid):
    if request.user.is_authenticated:
        cpobj = Cart_Product.objects.get(id = cpid)
        cpobj.cart_product_quantity -=1
        cpobj.save()
        return redirect('Show_Cart')
    else:
        return redirect('Home_page')

def remove_cp(request,cpid):
    if request.user.is_authenticated:
        cpobj = Cart_Product.objects.get(id = cpid)
        cpobj.delete()
        return redirect('Show_Cart')
    else:
        return redirect('Home_Page')