from django.db import models
from django.contrib.auth import  get_user_model
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# creates a profile for the user that prints the username of the user and their profile picture

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


# creating multiple user types to login/register - customer or business owner
    
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        CUSTOMER = 'CUSTOMER', 'Customer'
        BUSINESS = 'BUSINESS', 'Business'

    base_role = Role.ADMIN 

    role = models.CharField(max_length=50, choices=Role.choices)

    # arguments and key word arguments - custom workflow
    def save(self, *arg, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*arg, **kwargs)

class Customer(User):

    base_role = User.Role.CUSTOMER

    class Meta:
        proxy = True 
    
    def welcome(self):
        return "Only for customers"
