from django.db import models
from django.contrib.auth.models import AbstractUser


# this creates a class for the different users; the restaurant owners and the customer 
# with first and last name
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_restowner = models.BooleanField(default=False)
    first_name = models.charField(max_length=100)
    last_name = models.charField(max_length=100)


class customer(models.Model):
    user = models.OneToOneField(user,on_delete=models.CASCADE,primary_key=True)
    phone_number = models.CharField(max_length=13)
    location = models.CharField(max_length=20)

class is_restowner(models.Model):
    user = models.OneToOneField(user,on_delete=models.CASCADE,primary_key=True)
    phone_number = models.CharField(max_length=13)
    designation = models.CharField(max_length=20)