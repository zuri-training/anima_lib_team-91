<<<<<<< HEAD:user_auth/views.py
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
=======
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse

# from .models import User
from .forms import SigninUserForm


# Create your views here.
"""
def signin(request):
    if request.user.is_authenticated:                                               # if user is already signed in
        return redirect(reverse('home:home'))
    if request.method == 'POST':                                                    # after user submit the sign in form [POST]
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('home:home'))
        else:
            messages.error(request, 'Invalid login details. Try Again!')
            # messages.success(request, ('Invalid login details, try again!'))
            return redirect(reverse('user_auth:signin'))
    else:                                                                           # if user submit a GET request
        form = SigninUserForm()
    return render(request, 'user_auth/signin.html', {'form': form})



def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect(reverse('home:home'))
    return redirect(reverse('user_auth:signin'))
"""

"""
def signup(request):
    if request.user.is_authenticated:                                               # i.e user is already logged in
        return redirect(reverse('home:home'))
    if request.method == "POST":                                                    # when user submits the login form
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(
                request, "username already exist! please try another username")
            return redirect(reverse('user_auth:signup'))

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect(reverse('user_auth:signup'))

        if len(username) > 15:
            messages.error(request, "username must be under 15 characters!")
            return redirect(reverse('user_auth:signup'))

        if pass1 != pass2:
            messages.error(request, "Passwords didn't match")
            return redirect(reverse('user_auth:signup'))

        if not username.isalnum():
            messages.error(request, "Username can only contain alphabets or numerical characters")
            return redirect(reverse('user_auth:signup'))

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(
            request, "Your account has been successfully created.")

        return redirect(reverse('home:home'))

    return render(request, "user_auth/signup.html")
"""


# REFACTORING THE FORMS AND THEIR CORRESPONDING VIEWS
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

from .forms import SigninUserForm




# SIGNUP view
def signup(request):
    if request.method == 'POST':
        form = SigninUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account have been created successfully. You can login now.")
            return redirect(reverse('user_auth:signin'))
    else:
        form = SigninUserForm()
    return render(request, 'user_auth/signup.html', {'form': form})
    
>>>>>>> 44bd22b8c26dcfcc942740f23a0f9f65cf382706:Task Links/user_auth/views.py
