from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm 

# create a register view - uses request, passed to template, using a premade function that allows for the creation of a user
def register(request):
    if request.method == 'POST': 
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('main-home')
    else: 
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


