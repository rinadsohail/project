from django.db import models
from django.contrib.auth.models import AbstractUser


# this creates a class for the different users; the restaurant owners and the customer 
# with first and last name
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_restowner = models.BooleanField(default=False)

class customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    
class is_restowner(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    