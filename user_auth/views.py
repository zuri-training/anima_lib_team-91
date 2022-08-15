from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse

from .forms import SignupUserForm



# SIGNUP view
def signup(request):
    if request.method == 'POST':
        form = SignupUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account has been created for {username} successfully. You can login now.")
            return redirect(reverse('user_auth:signin'))
    else:
        form = SignupUserForm()
    return render(request, 'user_auth/signup.html', {'form': form, 'title': "Create Account"})


# SIGNIN VIEW
def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Signed in successfully. Welcome {user.username}.")
                return redirect(reverse('home:home'))
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    return render(request, 'user_auth/signin.html', {'form': form, 'title': "Log into your account"})
