from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from DRApps.web.views import *  # This imports all views from the web app


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        # Generate a unique username
        base_username = 'user'
        count = User.objects.filter(username__startswith=base_username).count()
        username = f"{base_username}{count + 1}"

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, f"Account created for {email}. Your username is {username}.")
        return redirect('login')
    return render(request, 'user/signup.html')
@csrf_protect
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            # Find user by email
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None
        if user is not None and user.check_password(password):
            # Authenticate the user with the custom backend
            user.backend = 'DRApps.user.backends.EmailBackend'  # Explicitly set the backend
            login(request, user)
            return redirect('manga_list')  # Redirect to the manga list page if login is successful
        else:
            messages.error(request, "Invalid email or password")  # Show error if login fails
    
    return render(request, 'user/login.html')
def logout_user(request):
    logout(request)
    return redirect('login')
  # Replace with your own web page

