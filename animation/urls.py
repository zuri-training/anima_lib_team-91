from django.urls import path

from . import views


app_name = "animation"

urlpatterns = [
    path('', views.display_animation, name='animation'), 
]