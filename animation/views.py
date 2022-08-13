from django.shortcuts import render

# Create your views here.
def display_animation(request):
    return render(request, 'animation/animation.html')