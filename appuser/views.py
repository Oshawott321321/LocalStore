from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm


from product.forms import ShopForm
from product.models import Shop

# Create your views here.

def register_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        # form = MYFORM(request.POST)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User Created')
    context = { 'form' : form }
    return render(request,'appuser/reg.html',context)

def login_user(request):
    form = AuthenticationForm()
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request = request , data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                passw = form.cleaned_data['password'] 
                user =  authenticate(username=name,password=passw)
                if user is not None:
                    login(request,user)
                    return redirect('Profile')
    else:
        return redirect('Profile')
    context = {'form':form}
    return render(request,'appuser/login.html',context)




def Profile(request):
    if request.user.is_superuser:
        if request.user.is_authenticated:
            users = OWNUSER.objects.all()
            if request.method == 'POST':
                form = AdminProfileForm(request.POST,instance = request.user)
                if form.is_valid():
                    form.save()
                    messages.success(request,"Profile Updated")
            form = AdminProfileForm(instance = request.user)
            shops = Shop.objects.filter(shop_owner =request.user)
            if not shops.exists():
                shops = None
            context={'form':form,'name':request.user , "users":users ,"shops":shops }
            return render(request,'appuser/profile.html',context)
        else:
            return redirect('Login')
    else:
        if request.user.is_authenticated:
            form = ProfileForm(instance = request.user)
            if request.method == 'POST':
                form = ProfileForm(request.POST,instance = request.user)
                if form.is_valid():
                    form.save()
                    messages.success(request,"Profile Updated")
            shops = Shop.objects.filter(shop_owner =request.user)
            if not shops.exists():
                shops = None
            context={'form':form,'name':request.user , "shops":shops }
            return render(request,'appuser/profile.html',context)
        else:
            return redirect('Login')

def log_out(request):
    logout(request)
    return redirect('Login')

def show_data(request,id):
    if request.user.is_authenticated:
        data = OWNUSER.objects.get(pk=id)
        form = AdminProfileForm(instance=data)
        context = {'form':form}
        return render(request,'appuser/user_data.html',context)
    else:
        return redirect('Login')

def change_pass(request):
    form = PasswordChangeForm(user=request.user)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                # update_session_auth_hash() THis function maintain the User profilr
                # If we dont use this then it will automatically log-out user 
                update_session_auth_hash(request,form.user)
                return redirect('Profile')            
    else:
        return redirect('Login')
    context={ 'form':form }
    return render (request,'appuser/changepass.html',context)

def change_pass1(request):
    #this one will not check  old password
    form = SetPasswordForm(user=request.user)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                # update_session_auth_hash() THis function maintain the User profilr
                # If we dont use this then it will automatically log-out user 
                update_session_auth_hash(request,form.user)
                return redirect('Profile')            
    else:
        return redirect('Login')
    context={ 'form':form }
    return render (request,'appuser/changepass1.html',context)


def create_shop(request):
    if not request.user.is_authenticated:
        return redirect('Home_Page')
    form = ShopForm(request.POST or None , request.FILES or None)
    if request.method == 'POST':
        form = ShopForm(request.POST,request.FILES)
        if form.is_valid():
            shopdata = form.save(commit=False)
            shopdata.shop_owner = request.user
            OWNUSER.objects.filter(username = request.user.username).update(is_shop_owner =True)
            shopdata.save()
            return redirect('Profile')
    context = {"form":form}
    return render(request,'appuser/create_shop.html',context)

def update_shop(request ,pk): # pk = shop id
    if not request.user.is_authenticated:
        return redirect('Login')
    
    shopdata = Shop.objects.get(id = pk)

    # confirming that is user is owner of shop or not
    if request.user.username != shopdata.shop_owner.username:
        return redirect('Home_Page')

    form = ShopForm(request.POST or None , request.FILES or None , instance=shopdata)
    if form.is_valid():
        form.save()
        print("shop Updated")
        return redirect('Myshop' ,pk = pk)
    context = {"form":form}
    return render(request,'appuser/update_shop.html',context)



# deletes Shop
def delete_shop(request,pk): #pk = Shop id
    if not request.user.is_authenticated:
        return redirect('Login')
    
    shopdata = Shop.objects.get(id = pk)

    # confirming that is user is owner of shop or not
    if request.user.username != shopdata.shop_owner.username:
        return redirect('Home_Page')
    shopdata.delete()
    tempshop_data = Shop.objects.filter(shop_owner= request.user)
    if not tempshop_data.exists():
        OWNUSER.objects.filter(username = request.user.username).update(is_shop_owner =False)
    return redirect('Profile')