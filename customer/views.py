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
    list_order = order.objects.filter(cname=request.user.username)
    context = {
        'list_order':list_order
    }
    return render(request,'customer/customer.html',context)

def orderupdate(request,pk):
    if request.method == 'POST':
        status_order = request.POST['order_status']
        print(status_order)
        print('HELLO')

        update_order=order.objects.get(pk=pk)

        update_order.order_status = status_order

        update_order.save()
        return redirect('customer')

    order_update = order.objects.get(pk=pk)
    context = {
        'order_update':order_update
    }
    return render(request,'customer/updateorder.html',context)

@login_required(login_url='login')
def booktaxi(request):
    if request.method == 'POST':
        from_desti = request.POST['from_desti']
        to_desti = request.POST['to_desti']
        date_to = request.POST['datepicker2']
        time_to = request.POST['time']

        print(request.user.username)
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

        
    driver_data = driver_detail.objects.filter(status='Available').order_by('id')
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
        time_to=cart_detail.time_to,
        order_status= 'Booked',
    )
    Order.save()
    return redirect('customer')
    list_order = order.objects.all()
    return render(request,'customer/orderlist.html')