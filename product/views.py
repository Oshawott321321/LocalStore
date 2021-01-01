from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import Http404
from .forms import *
from .models import *
from django.db.models import Q

# Create your views here.


def home_page(request):
    context = {}
    # Function call to fetch data
    # apply filters there
    product_data = Product.objects.all()
    context['product_data'] = product_data 
    return render(request,'product/home_page.html',context)

# 
# 
# 
# 
# 
# 
def search(request):
    query = request.GET['query']
    
    product_data = Product.objects.filter(Q(pro_name = query))

    shop_data = Shop.objects.filter(Q(shop_name__contains = query) | Q(shop_owner__username = query))
    
    context={"product_data" : product_data ,
                "shop_data" : shop_data}
    return render(request,'product/search.html',context)
# 
# 
# 
# 
# 
# 
# 
#     
# show details of shop to its owner and give options to modification
def myshop(request,pk): #pk = shop id  
    if not request.user.is_authenticated:
        return redirect('Login')
    
    try:
        shopdata = Shop.objects.get(id = pk)
    except:
        return redirect('Profile')

    # confirming that is user is owner of shop or not
    if request.user.username != shopdata.shop_owner.username:
        return redirect('Home_Page')
    products = Product.objects.filter(pro_shop = shopdata)
    context = {"pk":pk ,'shopdata':shopdata}

    if not products.exists():
        context['products'] = None
    else:
        context['products'] = products
    return render(request,"product/myshop.html",context)


def shop_details(request , pk): #pk =shop_id
    try:
        shop_data = Shop.objects.get(id = pk)
    except:
        return redirect('Home_Page')

    product_data = Product.objects.filter(pro_shop = shop_data)
    context = { "shop":shop_data , 
                "product_data":product_data}
    return render(request ,'product/shop_details.html',context)



# create product for particular shop
def create_product(request,pk):#pk = shop_id
    if not request.user.is_authenticated:
        return redirect('Login')

    
    # confirming that is user is owner of shop or not
    try:
        shopdata = Shop.objects.get(id = pk)
    except:
        return redirect('Profile')
    if request.user.username != shopdata.shop_owner.username:
        return redirect('Home_Page')
    # End check block
    
    form = ProductForm(request.POST or None , request.FILES or None)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            pdata = form.save(commit=False)
            pdata.pro_shop = Shop.objects.get(id = pk)
            pdata.save()
            return redirect('Myshop' ,pk =pk)

    context = { 'form':form ,'user':request.user ,"pk":pk}
    return render(request,'product/createproduct.html',context)



def update_product(request,pk): # pk = product id 

    # checking user authentication 
    if not request.user.is_authenticated:
        return redirect('Login')
    p = Product.objects.get(id = pk)
    if request.user.username != p.pro_shop.shop_owner.username:
        return redirect('Login')
    # End Check
        
    form = ProductForm( request.POST or None, instance=p)
    if form.is_valid():
        form.save()
        return redirect('Myshop' , pk = p.pro_shop.id)
    context = {"form":form}
    return render(request,"product/update_product.html",context)


def delete_product(request,pk): #pk = product_id
    if not request.user.is_authenticated:
        return redirect('Login')
    p = Product.objects.get(id = pk)
    if request.user.username != p.pro_shop.shop_owner.username:
        return redirect('Login')
    p.delete()
    return redirect('Myshop' ,pk = p.pro_shop.id)



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