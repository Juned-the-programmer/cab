from django.shortcuts import render,redirect
from . import views
from pages.decoraters import *
from .models import *
from django.contrib.auth.models import User,auth,Group,Permission
from customer.models  import *
# Create your views here.
def cabsignup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_no = request.POST['phone']
        username = request.POST['username']
        password = request.POST['username']
        pwd_repeat = request.POST['pwd-repeat']
        rick_no = request.POST['rick_no']
        your_image = request.FILES['your_image']
        rick_image = request.FILES['rick_image']

        if password == pwd_repeat:
            user = User.objects.create_user(username=username,password=password,first_name=name,is_staff=True)
            user.save()
            detail = driver_detail (
                name = name,
                email = email,
                phone_no = phone_no,
                username = username,
                password = password,
                rick_no = rick_no,
                your_image = your_image,
                rick_image = rick_image,
                status = "Available",
            )
            detail.save()
            group = Group.objects.get(name='cabdriver')
            user.groups.add(group)
            # permission =Permission.objects.get(staff)
            return redirect('index')
    return render(request,'cabdriver/cabsignup.html')


@allowed_users(allowed_roles=['cabdriver'])
def caborder(request):
    order_list = order.objects.filter(dname=request.user.username)
    context = {
        'order_list':order_list
    }
    return render(request,'cabdriver/caborders.html',context)