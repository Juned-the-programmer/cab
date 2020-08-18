from django.shortcuts import render
from pages.decoraters import *
from cabdriver.models import *
from pages.models import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
    return render(request,'customer/booktaxi.html')


@login_required(login_url='login')
def listdriver(request):
    if request.method == 'POST':
        from_desti = request.POST['from_desti']
        to_desti = request.POST['to_desti']
        date_to = request.POST['datepicker2']
        time_to = request.POST['time']

    driver_data = driver_detail.objects.all()
    context = {
        'driver_data':driver_data,
        'from_desti':from_desti,
        'to_desti':to_desti,
        'date_to':date_to,
        'time_to':time_to
    }
    return render(request,'customer/listdriver.html',context)
 
def orderlist(request,pk):    
    
    return render(request,'customer/orderlist.html')