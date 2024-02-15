from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# creates the user registration form that user must fill out - must fill out username, email, password and retyped password
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        