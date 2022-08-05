from django.urls import path

from . import views

urlpatterns = [
    path('', views.displayDocumentation, name='documentation')   
]