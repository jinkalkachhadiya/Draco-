from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import *

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Change 'home' to the name of your main page
    else:
        form = LoginForm()
    return render(request, 'web/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect('home')  # Redirect to home page or any other page after signup
    else:
        form = SignUpForm()
    return render(request, 'web/signup.html', {'form': form})