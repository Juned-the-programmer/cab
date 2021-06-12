from django.urls import path
from . import views
urlpatterns = [
    path('customer/',views.customer,name='customer'),
    path('booktaxi/',views.booktaxi,name='booktaxi'),
    path('listdriver/',views.listdriver,name='listdriver'),
    path('orderlist/<pk>',views.orderlist,name='orderlist'),
    path('orderupdate/<pk>',views.orderupdate,name='orderupdate')
]
