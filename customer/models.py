from django.db import models
from cabdriver.models import *
from pages.models import *
# Create your models here.
    
class order(models.Model):
    cname = models.CharField(max_length=50)
    dname = models.CharField(max_length=50)
    c_phone_no = models.CharField(max_length=50)
    d_phone_no = models.CharField(max_length=50)
    from_desti = models.CharField(max_length=50,null=True,blank=True)
    to_desti = models.CharField(max_length=50,null=True,blank=True)
    date_to = models.CharField(max_length=50,null=True,blank=True)
    time_to = models.CharField(max_length=50,null=True,blank=True)
    order_status = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.cname

class cart(models.Model):
    cname = models.CharField(max_length=50,null=True,blank=True)
    c_phone_no = models.IntegerField(null=True,blank=True)
    from_desti = models.CharField(max_length=50)
    to_desti = models.CharField( max_length=50)
    date_to = models.CharField(max_length=50)
    time_to = models.CharField(max_length=50)

    def __str__(self):
        return self.cname
    
    