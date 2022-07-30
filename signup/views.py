from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(
                request, "username already exist! please try another user name")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('home')

        if len(username) > 15:
            messages.error(request, "username must be under 15 characters!")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't match")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username must be either alpha-numerical")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(
            request, "your account has been successfully created.")

        return redirect('signin')

    return render(request, "signup/signup.html")
