from django.db import models

# Create your models here.
class Accounts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_no = models.IntegerField()
    Address = models.CharField(max_length=100)
    Area = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    