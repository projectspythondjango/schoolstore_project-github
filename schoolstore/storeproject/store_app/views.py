from django.contrib import messages, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
#
# from store_app.models import Department


# Create your views here.
# def index(request):
#     return HttpResponse("hai all")
def index(request):
        # departments=Department.objects.all()
        return render(request,'index.html')
def login(request):
    if request.method=='POST':
        name=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=name,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('store_app:user_page')
        else:
            messages.info(request,'Invalid User')
            return redirect('login')
    return render(request,'login.html')
def register(request):
        if request.method=='POST':
            name=request.POST['username']
            password=request.POST['password']
            cpassword=request.POST['confirmpassword']
            if password==cpassword:
                if User.objects.filter(username=name).exists():
                    messages.info(request,"Username Exists")
                    return redirect('store_app:register')
                else:
                    user=User.objects.create_user(username=name,password=password)
                    user.save()
                    return redirect('store_app:login')
            else:
                messages.info(request,"Passwords not matching")
                return redirect('store_app:register')
            return redirect('/')
        return render(request,'register.html')
def user_page(request):
    if request.method=='POST':
        messages.info(request,"Order Placed")
        return redirect('store_app:user_page')
    return render(request,'user.html')

def logout(request):
    auth.logout(request)
    return redirect('/')










