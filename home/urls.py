from django.urls import path

from . import views


# app_name = 'home' this line did not allow me to be able to use this name in the documentation app, maybe you should look at it

urlpatterns = [
    path('', views.home, name='home')                       # the website's homepage
]