from django.urls import path
from cabdriver import views

urlpatterns = [
    path('cabsignup/',views.cabsignup,name='cabsignup'),
    path('caborder/',views.caborder,name='caborder')
]
