from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# create a register view - uses request, passed to template, using a premade function that allows for the creation of a user
def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})