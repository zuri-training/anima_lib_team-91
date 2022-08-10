from django.urls import path

from . import views


app_name = 'user_auth'

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signup/',views.signup, name='signup' ),

]