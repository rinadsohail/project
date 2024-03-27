from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, BusinessRegisterForm

def register(request):
    if request.method == 'POST':
        # Determine user type based on form submission
        user_type = request.POST.get('user_type')
        # Choose form based on user type
        if user_type == 'personal':
            form = UserRegisterForm(request.POST)
        elif user_type == 'business':
            form = BusinessRegisterForm(request.POST)
        else:
            # Handle unexpected user type
            messages.error(request, 'Invalid user type.')
            return redirect('register')  # Redirect to registration page again
        
        # If form is valid, save the data
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created, {username}! You are now able to log in.')
            return redirect('login')
        else:
            # Handle form validation errors
            messages.error(request, 'Please correct the errors below.')
    else:
        # If it's a GET request, render the registration form
        form = UserRegisterForm()  # Default to personal form
    
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
