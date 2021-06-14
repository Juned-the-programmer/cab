from django.db import models

# Create your models here.
class driver_detail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254,blank=True)
    phone_no = models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    rick_no = models.CharField(max_length=50)
    your_image = models.ImageField(upload_to='static/img/driver_detail')
    rick_image = models.ImageField(upload_to='static/img/driver_detail')
    date_joined = models.DateField(auto_now_add=True , blank=True , null=True)
    status = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name
    