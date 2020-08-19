from django.shortcuts import render
from pages.decoraters import *
from cabdriver.models import *
from pages.models import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
# Create your views here.
@allowed_users(allowed_roles=['customer'])
@login_required(login_url='login')
def customer(request):
    taxi_driver = driver_detail.objects.all()
    context = {
        'taxi_driver':taxi_driver
    }
    return render(request,'customer/customer.html',context)

@login_required(login_url='login')
def booktaxi(request):
    if request.method == 'POST':
        from_desti = request.POST['from_desti']
        to_desti = request.POST['to_desti']
        date_to = request.POST['datepicker2']
        time_to = request.POST['time']
    
        data = Accounts.objects.get(name=request.user.username)
        try:
            if cart.objects.filter(cname=request.user.username).exists():
                cart.objects.get(cname=request.user.username).delete()
        except cart.DoesNotExist:
            None
        card_detail = cart (
            cname=request.user.username,
            c_phone_no=data.phone_no,
            from_desti = from_desti,
            to_desti= to_desti,
            date_to = date_to,
            time_to = time_to
        )
        card_detail.save()
        return redirect('listdriver')
    return render(request,'customer/booktaxi.html')


@login_required(login_url='login')
def listdriver(request):
    if request.method == 'POST':
        return redirect('orderlist')
    driver_data = driver_detail.objects.all().order_by('id')
    context = {
        'driver_data':driver_data
    }
    return render(request,'customer/listdriver.html',context)
 
def orderlist(request,pk):    
    customer_data = Accounts.objects.get(name=request.user.username)
    order_detail = driver_detail.objects.get(pk=pk)
    cart_detail = cart.objects.get(cname=request.user.username)
    Order = order (
        cname=request.user.username,
        dname=order_detail.name,
        c_phone_no=customer_data.phone_no,
        d_phone_no=order_detail.phone_no,
        from_desti=cart_detail.from_desti,
        to_desti=cart_detail.to_desti,
        date_to=cart_detail.date_to,
        time_to=cart_detail.time_to 
    )
    Order.save()
    context = {
        'order_detail':order_detail
    }
    return render(request,'customer/orderlist.html',context)