from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class BusinessRegisterForm(UserRegisterForm):
    # Add fields specific to business users here, e.g.,
    business_name = forms.CharField(max_length=100)