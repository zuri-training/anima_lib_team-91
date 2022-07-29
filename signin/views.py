from django.shortcuts import render, redirect
from .forms import signin_user
from django.contrib.auth import login, authenticate
from django.contrib import messages


def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('Invalid login details, try again!'))
            return redirect('signin')
    else:
        form = signin_user()
    return render(request, 'signin/signin.html', {'form': form})


