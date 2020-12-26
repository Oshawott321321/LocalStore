from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm

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
            context={'form':form,'name':request.user , "users":users }
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
            context={'form':form,'name':request.user }
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