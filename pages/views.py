from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,auth,Group
from django.contrib import messages
from datetime import datetime
# Create your views here.
def index(request):
    date = datetime.now()
    print(date)
    return render(request,'pages/index.html')

def about(request):
    return render(request,'pages/about.html')

def contact(request):
    return render(request,'pages/contact.html')

def service(request):
    return render(request,'pages/services.html')

def gallery(request):
    return render(request,'pages/gallery.html')

def signup(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_no = request.POST['phone']
        username = request.POST['username']
        pwd = request.POST['pwd']
        pwd_repeat = request.POST['pwd-repeat']
        Address = request.POST['Address']
        Area = request.POST['Area']

        if Accounts.objects.filter(username=username).exists():
            messages.error(request,'User already exists')
        else:
            if pwd == pwd_repeat:
                user = User.objects.create_user(first_name=name,username=username,email=email,password=pwd)
                user.save()

                customer = Accounts(
                    name = name,
                    email = email,
                    phone_no = phone_no,
                    username = username,
                    pwd = pwd,
                    Address = Address,
                    Area = Area
                )
                customer.save()
                group = Group.objects.get(name='customer')
                user.groups.add(group)
    return render(request,'pages/signup.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Enter Valid Username and Password')
            return redirect('login')
    return render(request,'pages/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')