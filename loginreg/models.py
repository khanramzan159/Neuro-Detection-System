from django.db import models
from django.db.models import Sum

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    status = models.IntegerField(default=1)
    
    # def __str__(self):
    #     return self.name
    
    
class Admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100) 